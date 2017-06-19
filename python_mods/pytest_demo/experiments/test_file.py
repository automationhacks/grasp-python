import pytest


@pytest.mark.setup_data({'Project': [{'dsn': 'xyz', 'env': 'some_env'}]})
def test_func():
    pass
