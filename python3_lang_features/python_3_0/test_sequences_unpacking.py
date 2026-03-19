def test_unpacking_sequences():
    # Before
    nums = [1, 2, 3, 4, 5]
    first = nums[0]
    rest = nums[1:-1]
    last = nums[-1]
    print(f'First: {first}, Rest: {rest}, Last: {last}')

    # After
    nums = [1, 2, 3, 4, 5]
    # * operator allows to unpack sequences more naturally
    first, *rest, last = nums
    print(f'First: {first}, Rest: {rest}, Last: {last}')