"""
自分のYouTube動画を一覧表示して、タイトル・公開設定を編集/一括変更するための
ローカルWebアプリ。

使い方:
    pip install -r requirements.txt
    python app.py
    ブラウザで http://127.0.0.1:5050 を開く

事前準備は README.md を参照。
"""
from flask import Flask, jsonify, render_template, request

import youtube_client

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/videos", methods=["GET"])
def api_list_videos():
    try:
        videos = youtube_client.list_my_videos()
        return jsonify({"ok": True, "videos": videos})
    except Exception as e:  # noqa: BLE001 - UIにエラー内容をそのまま出すため
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/playlists", methods=["GET"])
def api_list_playlists():
    """自分のプレイリスト一覧を取得（対象を絞り込む用のプルダウンに使う）。"""
    try:
        playlists = youtube_client.list_my_playlists()
        return jsonify({"ok": True, "playlists": playlists})
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/playlists/<playlist_id>/videos", methods=["GET"])
def api_list_playlist_videos(playlist_id):
    """指定プレイリストの中身だけを取得する。"""
    try:
        videos = youtube_client.list_videos_in_playlist(playlist_id)
        return jsonify({"ok": True, "videos": videos})
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/videos/<video_id>/current", methods=["GET"])
def api_get_current_state(video_id):
    """1本だけ現在の状態を取得する（保存前の食い違いチェック用、1 unitのみ消費）。"""
    try:
        state = youtube_client.get_current_state(video_id)
        return jsonify({"ok": True, **state})
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/videos/check_many", methods=["POST"])
def api_check_many():
    """複数動画の現在の状態をまとめて確認する（最大50件、1 unitのみ消費）。"""
    data = request.get_json(force=True) or {}
    ids = data.get("ids", [])
    try:
        states = youtube_client.get_current_states(ids)
        return jsonify({"ok": True, "states": states})
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/videos/<video_id>", methods=["POST"])
def api_update_video(video_id):
    data = request.get_json(force=True) or {}
    title = data.get("title")
    privacy_status = data.get("privacyStatus")
    try:
        youtube_client.update_video(video_id, title=title, privacy_status=privacy_status)
        return jsonify({"ok": True, "id": video_id})
    except Exception as e:  # noqa: BLE001
        return jsonify({"ok": False, "id": video_id, "error": str(e)}), 500


@app.route("/api/videos/bulk_privacy", methods=["POST"])
def api_bulk_privacy():
    data = request.get_json(force=True) or {}
    ids = data.get("ids", [])
    privacy_status = data.get("privacyStatus")

    results = []
    for video_id in ids:
        try:
            youtube_client.update_privacy_status(video_id, privacy_status)
            results.append({"id": video_id, "ok": True})
        except Exception as e:  # noqa: BLE001
            results.append({"id": video_id, "ok": False, "error": str(e)})

    return jsonify({"ok": True, "results": results})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
