import pytest


@pytest.fixture()
def username(username):
    return 'overridden-else-' + username


def test_user_name(username):
    assert username == 'overridden-else-username'
