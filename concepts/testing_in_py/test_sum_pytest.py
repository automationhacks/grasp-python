def test_sum():
    assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum_tuple(benchmark):
    result = benchmark(sum((1, 2, 3)))
    assert result == 6, 'Should be 6'
