from nose.tools import assert_true
import requests


def test_request_response():
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    assert_true(response.ok)