import json
import os
import pathlib
import time

from dotenv import load_dotenv
from mastodon import Mastodon

from truthbrush import Api

load_dotenv(".env.local")


def get_access_token(email: str, passwd: str) -> str:
    """アクセストークンの取得と永続化"""
    data_path = pathlib.Path("data.local")
    if data_path.exists():
        with open(data_path, mode="r") as f:
            data = json.load(f)
            if "access_token" in data:
                return data["access_token"]
    with open(data_path, mode="w") as f:
        # なければ取得
        truth = Api(email, passwd)
        access_token = truth.get_auth_id(email, passwd)
        json.dump({"access_token": access_token}, f)
        return access_token


email = os.environ["EMAIL"]
passwd = os.environ["PASSWD"]
if not email or not passwd:
    print("Set EMAIL and PASSWD in env or .env.local")

access_token = get_access_token(email, passwd)

# 初期化
time.sleep(1)

print(access_token)
api = Mastodon(
    api_base_url="https://truthsocial.com",
    client_id="9X1Fdd-pxNsAgEDNi_SfhJWi8T-vLuV2WVzKIbkTCw4",
    client_secret="ozF8jzI4968oTKFkEnsBC-UbLPCdrSv0MkXGQu2o_-M",
    access_token=access_token,
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
)

api.toot("Hello World Mastodon.pyから投稿")
