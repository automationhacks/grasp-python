"""
Apply indirect on particular arguments
"""

import pytest


@pytest.mark.parametrize('get_cert', [('a_dsn', 'some_uname', 'some_pwd')], indirect=['get_cert'])
def test_indirect(get_cert):
    print('i am inside test func')
    print(get_cert)
