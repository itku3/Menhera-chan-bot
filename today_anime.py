import hashlib
import time
from urllib.parse import urlencode
import jwt
import requests
import uuid
import os
data = []


def getTodayAnime():
    url = "https://api.OHLI.moe/anitime/list?w="+time.strftime("%w")
    # print(time.strftime("%w"))
    response = requests.request("GET", url)

    for i in response.json():
        data.append(i['s'])
    return data

# getTodayAnime()
