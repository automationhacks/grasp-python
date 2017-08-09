# """
# sort a list of numbers but prioritize one group of numbers to come first
# """
# pass a helper function as the key argument to a list’s sort method

#
# def sort_priority(values, groups):
#
#     def helper(x):
#         if x in groups:
#             return 0, x
#         return 1, x
#
#     values.sort(key=helper)
#
#
# def sort_priority2(values, groups):
#     found = False
#
#     def helper(x):
#         nonlocal found  # The nonlocal statement makes it clear when data is being assigned out of a closure into another scope
#         if x in groups:
#             found = True
#             return 0, x
#         return 1, x
#     values.sort(key=helper)
#     return found
#
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# groups = {2, 3, 5, 7}
#
# sort_priority(numbers, groups)
# print(numbers)
# sort_priority2(numbers, groups)
# print(numbers)


class Sorter(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sorter = Sorter(group)
print(numbers.sort(key=sorter))
assert sorter.found is True
