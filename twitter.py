import hashlib
import time
from urllib.parse import urlencode
import jwt
import requests
import uuid
import os
data = []


def getTwitterProfile():
    url = "https://api.twitter.com/1.1/users/show.json"
    # print(time.strftime("%w"))
    querystring = {"user_id": 1009472287718772736, "screen_name": "__ITKU"}

    response = requests.request("GET", url, params=querystring)

    print(response.json())
