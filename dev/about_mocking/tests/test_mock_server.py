from unittest.mock import patch

from nose.tools import assert_true, assert_dict_contains_subset, \
    assert_list_equal

from dev.about_mocking.mocks import get_free_port, start_mock_server
from dev.about_mocking.services import get_users
from unittest.mock import patch

from nose.tools import assert_true, assert_dict_contains_subset, \
    assert_list_equal

from dev.about_mocking.mocks import get_free_port, start_mock_server
from dev.about_mocking.services import get_users


class TestMockServer:

    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_request_response(self):
        url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        with patch.dict('dev.about_mocking.services.__dict__',
                        {'USERS_URL': url}):
            response = get_users()

        assert_true(response.ok)
        expected_headers = {'Content-Type': 'application/json; charset=utf-8'}
        assert_dict_contains_subset(expected_headers, response.headers)
        assert_list_equal(response.json(), [])
