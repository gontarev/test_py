import pytest
import requests
import json


def test_post_headers_body_json():
    url = 'https://httpbin.org/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {'key1': 1, 'key2': 'value2'}

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers = headers, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)

@pytest.fixture
def fixt1():
    print("\nInitialization of fixture")
    fixture = "I am fixture"
    yield fixture
    print("\nDestroying of fixture")

def test_1(fixt1):
    print('- test_1()')
    assert fixt1

def test_2(fixt1):
    print('- test_2()')
    assert 1 == 1

def test_3(fixt1):
    print('- test_3()')
    assert fixt1 == "I am fixture"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_int_convert():
    s = "вфыпыапв"
    with pytest.raises(ValueError) as excinfo:
        i = int(s)
    assert 'invalid literal for int() with base 10' in str(excinfo.value)
    print('\n- test_4')