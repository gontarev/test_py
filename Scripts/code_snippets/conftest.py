import pytest
import requests

from Scripts.code_snippets.test_registration import base_url


@pytest.fixture()
def get_registration_cookies():
    url = base_url + "/registration"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers)

    # print(response.text.encode('utf8'))
    cookies = response.headers.get('Set-Cookie')
    print(response.headers.get('Set-Cookie'))

    return cookies
