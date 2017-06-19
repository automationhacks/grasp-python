import pytest


@pytest.mark.parametrize('test_input, expected',
                         [('3+5', 8), ('2+4', 6),
                          # pytest.param('6*2', 11, marks=pytest.mark.xfail), ])  # Supported in pytest 3.1 onwards
                          pytest.mark.xfail(('6*2', 11))])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
