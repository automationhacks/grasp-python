
def sort_priority(values, groups):
    found = False
    def helper(x):
        nonlocal found
        if x in groups:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
groups = {2, 3, 5, 7}

f = sort_priority(numbers, groups)
print(numbers, f)
