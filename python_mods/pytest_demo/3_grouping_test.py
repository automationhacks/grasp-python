"""
tests can be logically grouped in a class
Remember:
    1. Class should be Test prefixed
    2. Class should not have __init__
    3. Methods should be test_ prefixed
    4. Methods in above mentioned class or outside will be picked
    5. Module should be either _test suffixed or test_ prefixed (strict)
"""


class TestClass(object):
    def test_one(self):
        x = 'This'
        assert 'h' in x

    def test_second(self):
        x = 'hello'
        assert hasattr(x, 'check')


def test_three():
    assert 0  # demo purposes
