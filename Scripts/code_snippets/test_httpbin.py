import json

import requests

url = 'http://httpbin.org/get'
payload = {'key1': 'value'}
r = requests.get(url, params=payload)
print(r.text)

to_dict = r.json()
# print(type(to_dict))
# print(to_dict)
to_resp = json.dumps(to_dict)
to_obj = json.loads(to_resp)
# to_resp = json.loads(str(to_dict))
print(to_obj)
print(type(r))
print(type(r.text))
print(type(to_dict))
print(type(to_resp))
print(type(to_obj))
# print(to_dict['headers'])
# print(to_dict['headers']['User-Agent'])

range