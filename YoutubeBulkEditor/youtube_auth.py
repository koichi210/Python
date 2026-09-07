"""
YouTube Data API v3 の認証まわり。

初回実行時はブラウザが開いてGoogleアカウントでのログイン・同意を求められる。
以降は token.json に保存された認証情報を使い回す（有効期限が切れたら自動更新）。
"""
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "client_secret.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")

# 動画のタイトル変更・公開設定変更に必要なスコープ
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def get_authenticated_service():
    """認証済みの YouTube API クライアントを返す。"""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRET_FILE):
                raise FileNotFoundError(
                    f"{CLIENT_SECRET_FILE} が見つからないよ！\n"
                    "Google Cloud Console で OAuth クライアントID（デスクトップアプリ）を作成して、\n"
                    "ダウンロードしたJSONを client_secret.json という名前でこのフォルダに置いてね。"
                )
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # 次回以降のために保存
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            f.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)
