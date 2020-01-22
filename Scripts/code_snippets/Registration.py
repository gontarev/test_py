import json

import requests

url = "http://accounts-new.dev.ukr.net/registration"

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers)

# print(response.text.encode('utf8'))
cookie = response.headers.get('Set-Cookie')
print(response.headers.get('Set-Cookie'))


################################################################################
url = "https://accounts-new.dev.ukr.net/api/v1/registration/reserve_login"

# cookie_name = "ars"
# cookie_value = "K2owOA.ZGIwOE9COGdLeW91SFBTNkI1eWdjbzFHTzU2bG05eFo"
# cookie = "ars=K2owOA.ZGIwOE9COGdLeW91SFBTNkI1eWdjbzFHTzU2bG05eFo"
payload = "{\"login\":\"test\"}"
headers = {
    'Content-Type': 'application/json',
    'Cookie': cookie
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
# print(response.headers)
# print(response.headers.get('Date'))
# json.dumps()