from nose.tools import assert_true, assert_dict_contains_subset, \
    assert_is_instance

from dev.about_mocking.services import get_users


def test_request_response():
    response = get_users()

    assert_true(response.ok)
    expected_headers = {'Content-Type': 'application/json; charset=utf-8'}
    assert_dict_contains_subset(expected_headers, response.headers)
    assert_is_instance(response.json(), list)
