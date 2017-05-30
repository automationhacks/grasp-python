"""
if you want to assert that some code raises an exception you can use the raises helper
"""
import pytest


def foo():
    raise SystemExit(1)


def test_foo():
    with pytest.raises(SystemExit):
        foo()

# Run in quiet mode pytest -q 2_exception_test.py
# This will ensure less information is displayed after run
