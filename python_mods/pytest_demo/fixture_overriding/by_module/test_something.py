import pytest


@pytest.fixture()
def username(username):
    return 'overridden-' + username


def test_user_name(username):
    assert username == 'overridden-username'
