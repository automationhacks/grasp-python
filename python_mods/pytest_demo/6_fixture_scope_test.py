import pytest
import assertpy

"""
scope=module ensures fixture func is called once per module,
and value is shared by all test functions

these fixtures can be moved to separate conftest.py file such that,
it can be accessible from different modules.
"""


@pytest.fixture(scope='module')
def get_cur_date():
    import datetime
    return datetime.datetime.now()


def test_current_date(get_cur_date):
    assert get_cur_date
    assert 0  # for demo purposes


def test_another_date(get_cur_date):
    assertpy.assert_that(get_cur_date is not None)
    assert 0  # again for demo
