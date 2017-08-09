"""
Be defensive while iterating over arguments
"""

# Program to find the percentage contribution of city to overall tourism nos

# Basic impl
visits = [15, 35, 80]


def normalize(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percentage = 100 * value / total
        result.append(percentage)
    return result


# print(normalize(visits))


# To scale the above, we should read from a file with data for every city in texas

def read_visits(path):
    with open(path) as f:
        for line in f:
            yield int(line)  # yield a generator

# it = read_visits('tourism.txt')
# print(list(it))
# print(list(it))

# percentages = normalize(it)
# print(percentages) # This prints [] iterator produces results a single time, if you iterate
# over an iterator or generator which has raised StopIteration exception, you would not get results a 2nd time
# (Ln 32/33)

# To solve above problem, we can keep a copy of the entire content in a list


def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = [100 * value / total for value in numbers]
    return result

it = read_visits('tourism.txt')
# print(normalize_copy(it))

# Problem with above approach is that if contents of the iterator is large, copying it in memory would result in
# system crash

# One way to solve this is to accept a func which returns an iterator every time


def normalize_func(get_iter):
    total = sum(get_iter())  # New iter
    result = [100 * value / total for value in get_iter()]  # Another iter
    return result

# lambda func which calls generator and returns a new iterator every time
percentages = normalize_func(lambda: read_visits('tourism.txt'))
print('% thru new iterator ', percentages)

# This method, although it works seems clumsy, a better way would be to implement a container class which
# implements iterator protocol

