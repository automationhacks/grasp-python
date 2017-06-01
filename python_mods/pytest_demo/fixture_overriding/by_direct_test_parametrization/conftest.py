import pytest


@pytest.fixture()
def username():
    return 'username'


@pytest.fixture()
def other_username(username):
    return 'other-' + username


