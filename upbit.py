import hashlib
from urllib.parse import urlencode
import requests


# ACCESS_KEY = open("token/upbit-token.txt", 'r').readline(1)
# SECRET_KEY = open("token/upbit-token.txt", 'r').readline(2)

def getCoinName(text):
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    market_dict = {}
    for i in response.json():
        if i['market'].split("-")[0] == "KRW":
            market_dict[i['korean_name']] = i['market']
        else:
            continue
    return market_dict[text]


def getTradePrice(market):
    url = "https://api.upbit.com/v1/candles/days"
    querystring = {"market": market, "count": "1"}

    response = requests.request("GET", url, params=querystring)
    return response.json()[0]['trade_price']
