from concepts.testing_in_py.my_sum import do_sum


def test_sum():
    assert do_sum([1, 2, 3]) == 6, 'Should be 6'
