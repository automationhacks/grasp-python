import pytest


def pytest_generate_tests(metafunc):
    # called once per test func
    func_args = metafunc.cls.params[metafunc.function.__name__]
    arg_names = sorted(func_args[0])
    metafunc.parametrize(arg_names, [[func_arg[name] for name in arg_names]
                                     for func_arg in func_args])


class TestClass(object):
    params = {
        'test_equals': [{'a': 1, 'b': 2}, {'a': 3, 'b': 3}, ],
        'test_zero_division': [{'a': 1, 'b': 0}]
    }

    def test_equals(self, a, b):
        assert a == b

    def test_zero_division(self, a, b):
        pytest.raises(ZeroDivisionError, 'a/b')