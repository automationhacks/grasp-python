def foo():
    assert 0


def bar():
    raise NameError()


def test_foo():
    print('Step 1')
    print('Step 2')
    foo()
    bar()


def test_happy():
    pass
