import os
from truthbrush import Api
from mastodon import Mastodon
import time
from dotenv import load_dotenv

load_dotenv(".env.local")

email = os.environ["EMAIL"]
passwd = os.environ["PASSWD"]
if not email or not passwd:
    print("Set EMAIL and PASSWD in env or .env.local")

truth = Api(email, passwd)
access_token = truth.get_auth_id(email, passwd)

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
