# Write program to find index of every word in string

string = 'This is a sample program'


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


print(index_words(string))


# Better approach would be using generators:
#
# Generators are functions that use yield expressions.
# When called, generator functions do not actually run but instead immediately return an iterator.
# With each call to the next built-in function, the iterator will advance the generator to its next yield expression.
# Each value passed to yield by the generator will be returned by the iterator to the caller.

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result = list(index_words_iter(string))
print(result)


# Discussion:
# The second problem with index_words is that it requires all results to
# be stored in the list before being returned. For huge inputs, this can
# cause your program to run out of memory and crash. In contrast, a
# generator version of this function can easily be adapted to take inputs
# of arbitrary length.

# Exercise: Write generator that returns offset per line at a time

def index_file_iter(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('sample.txt', 'r') as f:
    it = index_file_iter(f)
    print(list(it)[0: 3])

# The only gotcha of defining generators like this is that the callers
# must be aware that the iterators returned are stateful and can’t be
# reused

# Things to Remember
# ✦ Using generators can be clearer than the alternative of returning
# lists of accumulated results.
# ✦ The iterator returned by a generator produces the set of values
# passed to yield expressions within the generator function’s body.
# ✦ Generators can produce a sequence of outputs for arbitrarily large
# inputs because their working memory doesn’t include all inputs and
# outputs.
