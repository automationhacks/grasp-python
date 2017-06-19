import pytest


@pytest.fixture()
def foo(foobar, bar):
    pass


@pytest.fixture()
def bar(request):
    print(request.function.__name__)
    print('Inside bar', request)


@pytest.fixture()
def foobar():
    get_me = 'Did you get me?'
