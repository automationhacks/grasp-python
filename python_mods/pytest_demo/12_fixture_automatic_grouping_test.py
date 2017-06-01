import pytest


@pytest.fixture(scope='module', params=['mod1', 'mod2'])
def modarg(request):
    param = request.param
    print('setup modarg %s\n' % param)
    yield param
    print('teardown modarg %s\n' % param)


@pytest.fixture(scope='function', params=[1, 2])
def otherarg(request):
    param = request.param
    print('setup otherarg %s\n' % param)
    yield param
    print('teardown otherarg %s\n' % param)


def test_0(otherarg):
    print('test_0 with otherarg %s\n' % otherarg)


def test_1(modarg):
    print('test_1 with modarg %s\n' % modarg)


def test_2(otherarg, modarg):
    print('test_2 with otherarg %s and modarg %s' % (otherarg, modarg))
