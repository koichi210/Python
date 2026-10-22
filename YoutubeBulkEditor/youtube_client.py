"""
YouTube Data API v3 を叩く処理をまとめたモジュール。
"""
from youtube_auth import get_authenticated_service


def _fetch_video_details(youtube, video_ids):
    """video_ids（最大50件ずつ）から詳細情報を取得して一覧化する共通処理。"""
    videos = []
    for i in range(0, len(video_ids), 50):
        chunk = video_ids[i : i + 50]
        response = (
            youtube.videos()
            .list(part="snippet,status,statistics", id=",".join(chunk))
            .execute()
        )
        for item in response.get("items", []):
            snippet = item["snippet"]
            status = item["status"]
            statistics = item.get("statistics", {})
            thumbnails = snippet.get("thumbnails", {})
            thumb = (
                thumbnails.get("default", {}).get("url")
                or thumbnails.get("medium", {}).get("url")
                or ""
            )
            # いいね数を非公開にしている動画は likeCount が返ってこない
            like_count = statistics.get("likeCount")
            videos.append(
                {
                    "id": item["id"],
                    "title": snippet.get("title", ""),
                    "privacyStatus": status.get("privacyStatus", ""),
                    "uploadStatus": status.get("uploadStatus", ""),
                    "thumbnail": thumb,
                    "publishedAt": snippet.get("publishedAt", ""),
                    "likeCount": int(like_count) if like_count is not None else None,
                }
            )
    return videos


def _get_video_ids_from_playlist(youtube, playlist_id):
    """指定プレイリストの中身（動画ID）を全ページ集める（1ページ1 unit）。"""
    video_ids = []
    page_token = None
    while True:
        response = (
            youtube.playlistItems()
            .list(
                part="contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=page_token,
            )
            .execute()
        )
        for item in response.get("items", []):
            video_ids.append(item["contentDetails"]["videoId"])

        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return video_ids


def list_my_playlists():
    """
    自分が持ってるプレイリスト一覧を取得する（1ページ1 unit）。
    「ドラフト識別用に作った専用プレイリスト」を選んでもらうための一覧表示用。

    戻り値: [{id, title, itemCount}, ...]
    """
    youtube = get_authenticated_service()

    playlists = []
    page_token = None
    while True:
        response = (
            youtube.playlists()
            .list(part="snippet,contentDetails", mine=True, maxResults=50, pageToken=page_token)
            .execute()
        )
        for item in response.get("items", []):
            playlists.append(
                {
                    "id": item["id"],
                    "title": item["snippet"]["title"],
                    "itemCount": item["contentDetails"].get("itemCount", 0),
                }
            )
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return playlists


def list_videos_in_playlist(playlist_id):
    """
    指定した1つのプレイリストの中身だけを取得する。
    「ドラフトだけを集めた専用プレイリスト」を対象にすれば、
    Studio自身が判定した「ドラフト」の集合をそのまま扱える。

    戻り値: list_my_videos() と同じ形式
    """
    youtube = get_authenticated_service()
    video_ids = _get_video_ids_from_playlist(youtube, playlist_id)
    videos = _fetch_video_details(youtube, video_ids)
    videos.sort(key=lambda v: v["publishedAt"], reverse=True)
    return videos


def list_my_videos():
    """
    自分のチャンネルの動画を全件取得して返す。
    公開・限定公開・非公開・ドラフト、すべて対象のはず。

    動画IDの列挙は「アップロード済み動画」プレイリスト（playlistItems.list、
    1ページ1 unit）を使う。search.list（1ページ100 unit）よりはるかに安い。
    ※もしオーナーでもこのプレイリストに一部の動画（ドラフト等）が
    含まれないケースが見つかったら、list_my_videos_via_search() に戻すこと。

    戻り値: [{id, title, privacyStatus, uploadStatus,
              thumbnail, publishedAt, likeCount}, ...]
    """
    youtube = get_authenticated_service()

    # 1. 自分のチャンネルの「アップロード済み動画」プレイリストIDを取得（1 unit）
    channels_response = (
        youtube.channels().list(part="contentDetails", mine=True).execute()
    )
    items = channels_response.get("items", [])
    if not items:
        raise ValueError("チャンネル情報が取得できなかったよ")
    uploads_playlist_id = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # 2. そのプレイリストの中身（＝自分の全動画）のIDを集める
    video_ids = _get_video_ids_from_playlist(youtube, uploads_playlist_id)

    # 3. videos.list は1回で最大50件・1 unitと軽いので、50件ずつまとめて詳細取得
    videos = _fetch_video_details(youtube, video_ids)

    # 公開日時の新しい順に並べておく
    videos.sort(key=lambda v: v["publishedAt"], reverse=True)
    return videos


def list_my_videos_via_search():
    """
    list_my_videos() のフォールバック版。search.list(forMine=True) で動画IDを
    列挙する（1ページ100 unitと高コストだが、プレイリスト方式より確実に
    全動画を拾える可能性が高い）。プレイリスト方式で件数が合わない時用に残してある。
    """
    youtube = get_authenticated_service()

    video_ids = []
    page_token = None
    while True:
        response = (
            youtube.search()
            .list(
                part="id",
                forMine=True,
                type="video",
                maxResults=50,
                pageToken=page_token,
            )
            .execute()
        )
        for item in response.get("items", []):
            video_ids.append(item["id"]["videoId"])

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    videos = _fetch_video_details(youtube, video_ids)
    videos.sort(key=lambda v: v["publishedAt"], reverse=True)
    return videos


def get_current_states(video_ids):
    """
    複数動画の現在のタイトル・公開設定をまとめて取得する（最大50件まで、1 unitのみ消費）。
    「まとめて保存」の食い違いチェックをバッチ化するための関数。

    戻り値: {video_id: {title, privacyStatus}, ...}
    """
    if not video_ids:
        return {}
    if len(video_ids) > 50:
        raise ValueError("一度に確認できるのは50件までだよ")

    youtube = get_authenticated_service()
    response = (
        youtube.videos()
        .list(part="snippet,status", id=",".join(video_ids))
        .execute()
    )
    result = {}
    for item in response.get("items", []):
        result[item["id"]] = {
            "title": item["snippet"].get("title", ""),
            "privacyStatus": item["status"].get("privacyStatus", ""),
        }
    return result


def get_current_state(video_id):
    """
    1本だけの現在のタイトル・公開設定を取得する（videos.listは1件でも1 unitと軽い）。
    キャッシュ表示中の内容と、YouTube側の実際の最新状態がズレていないか確認する用途。
    """
    youtube = get_authenticated_service()
    response = (
        youtube.videos().list(part="snippet,status", id=video_id).execute()
    )
    items = response.get("items", [])
    if not items:
        raise ValueError(f"動画が見つからないよ: {video_id}")

    snippet = items[0]["snippet"]
    status = items[0]["status"]
    return {
        "title": snippet.get("title", ""),
        "privacyStatus": status.get("privacyStatus", ""),
    }


def update_privacy_status(video_id, privacy_status):
    """
    公開設定だけを変更する（タイトル等はそのまま）。
    status も update 時に丸ごと置き換わる仕様で、privacyStatus だけ送ると
    埋め込み許可・ライセンス・子ども向け設定などが既定値に戻ってしまうので、
    update_video() と同じく現在値を取得してから privacyStatus だけ書き換える。
    """
    youtube = get_authenticated_service()

    current = youtube.videos().list(part="status", id=video_id).execute()
    items = current.get("items", [])
    if not items:
        raise ValueError(f"動画が見つからないよ: {video_id}")

    status = items[0]["status"]
    status["privacyStatus"] = privacy_status
    # 予約公開日時(publishAt)は非公開の動画にしか設定できない。
    # 以前の実装と同じく、非公開以外へ変える時は予約を外す。
    if privacy_status != "private":
        status.pop("publishAt", None)

    youtube.videos().update(
        part="status",
        body={"id": video_id, "status": status},
    ).execute()


def update_video(video_id, title=None, privacy_status=None):
    """
    タイトル・公開設定をまとめて変更する。
    snippet は update 時に丸ごと置き換わる仕様なので、先に現在値を取得してから
    必要な項目だけ書き換えて送り直す（read-modify-write）。
    """
    youtube = get_authenticated_service()

    current = (
        youtube.videos()
        .list(part="snippet,status", id=video_id)
        .execute()
    )
    items = current.get("items", [])
    if not items:
        raise ValueError(f"動画が見つからないよ: {video_id}")

    snippet = items[0]["snippet"]
    status = items[0]["status"]

    if title is not None:
        snippet["title"] = title
    if privacy_status is not None:
        status["privacyStatus"] = privacy_status

    youtube.videos().update(
        part="snippet,status",
        body={"id": video_id, "snippet": snippet, "status": status},
    ).execute()
