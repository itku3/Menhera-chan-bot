from urllib.parse import urlencode
import requests


key = "e6c2110d0c9adc7af18417e3aaa3fe3e40ebb402"


def getUserid_and_profileimage(text):

    url = "https://osu.ppy.sh/api/get_user"
    querystring = {"u": text, "k": key}

    response = requests.request("GET", url, params=querystring)
    user_id = response.json()[0]['user_id']

    return "http://s.ppy.sh/a/"+user_id
