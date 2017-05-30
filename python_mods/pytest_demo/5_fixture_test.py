import pytest


@pytest.fixture
def get_current_date():
    import datetime
    return datetime.datetime.now()


def test_current_date(get_current_date):
    assert get_current_date
    assert 0  # for demo purposes
