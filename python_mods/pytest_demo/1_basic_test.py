# Func under test
def inc(x):
    return x + 1


# test cases
def test_wrong_answer():
    assert inc(3) == 5


def test_correct_answer():
    assert inc(4) == 5
