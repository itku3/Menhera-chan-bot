from urllib.parse import urlencode
import requests


key = open("osu-token.txt", 'r').read()


def getUserid_and_profileimage(text):

    url = "https://osu.ppy.sh/api/get_user"
    querystring = {"u": text, "k": key}

    response = requests.request("GET", url, params=querystring)
    user_id = response.json()[0]['user_id']

    return "http://s.ppy.sh/a/"+user_id
