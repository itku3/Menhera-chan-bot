import os
import sys
from typing import Text
import urllib.request

client_id = "fRFSaFenNdZ1XBGIre4L"
client_secret = "M1npKBsmBT"


def check_lang(text):
    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    langcode = []
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        langcode = response_body.decode('utf-8').split("\"")
        return langcode[3]
    else:
        print("Error Code:" + rescode)


def romoji():
    encText = urllib.parse.quote("안녕")
    url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


def translate():
    encText = urllib.parse.quote("반갑습니다")
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        papago_lang = response_body.decode('utf-8').split("\"")
        print(papago_lang[27])
    else:
        print("Error Code:" + rescode)


def ja_to_ko(text):
    encText = urllib.parse.quote(text)
    data = "source=ja&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        papago_lang = response_body.decode('utf-8').split("\"")
        return (papago_lang[27])
    else:
        return ("Error Code:" + rescode)


def ko_to_ja(text):
    encText = urllib.parse.quote(text)
    data = "source=ko&target=ja&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        papago_lang = response_body.decode('utf-8').split("\"")
        return (papago_lang[27])
    else:
        return ("Error Code:" + rescode)
