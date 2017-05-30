def flaky_func():
    try:
        a = 5 / 0
    except ZeroDivisionError as e:
        print('flaky func failed because of %s' % e)
        # raise
    else:
        return a
    finally:
        print('Inside finally for flaky_func()')


def flaky_func1():
    a = {'a': 1}
    try:
        # return 5 / 0
        print(a['b'])
    except ZeroDivisionError as e:
        print('Exception details', e)
        # raise
    finally:
        print('Inside finally for flaky_func1()')
