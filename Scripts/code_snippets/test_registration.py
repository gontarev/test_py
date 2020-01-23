import json
import random
import string

import requests

base_url = "https://accounts-new.dev.ukr.net"
url = "https://accounts-new.dev.ukr.net/api/v1/registration/reserve_login"


def test_used_login(get_registration_cookies):
    payload = "{\"login\":\"test\"}"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': get_registration_cookies
    }

    response = requests.request("POST", base_url + "/api/v1/registration/reserve_login", headers=headers, data=payload)

    print(response.text.encode('utf8'))
    resp_body = response.json()
    assert resp_body['available'] is False


# print(response.headers)
# print(response.headers.get('Date'))
# json.dumps()

def test_unused_login(get_registration_cookies):
    payload = "{\"login\":\"" + ''.join(random.choices(string.ascii_letters + string.digits, k = random.randrange(1, 32))) + "\"}"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': get_registration_cookies
    }

    response = requests.request("POST", base_url + "/api/v1/registration/reserve_login", headers=headers, data=payload)

    print(payload)
    print(response.text.encode('utf8'))
    resp_body = response.json()
    assert resp_body['available'] is True
