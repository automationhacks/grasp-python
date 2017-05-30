# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# squares = [x**2 for x in a]
# print(squares)
#
# map_squares = map(lambda x: x ** 2, a)
# print(list(map_squares))
#
# squares_even = [x ** 2 for x in a if x % 2 == 0]
# print(squares_even)
#
# squares_even_map_filters = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
# print(list(squares_even_map_filters))

# assert squares_even == list(squares_even_map_filters) # AssertionError

# chile_ranks = {'ghost': 1,
#                'habanero': 2,
#                'cayenne': 3}
#
# rank_dict = {rank: name for name, rank in chile_ranks.items()}
# chile_len_set = {len(name) for name in rank_dict.values()}
#
# print(rank_dict)
# print(chile_len_set)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# flat = [x for row in matrix for x in row]
# flat1 = []
#
# for row in matrix:
#     for x in row:
#         flat1.append(x)
#
# print(flat)
# print(flat1)
#
# for row in matrix:
#     for x in row:
#         x = x**2
#
# print(matrix)

"""
Filter a list of numbers to only even values greater than four
"""

# a = [x for x in range(1, 100)]
# b = [i for i in a if i % 2 == 0 if i > 4] # Note - and is not mandatory but can be given optionally between if's
# print('b= ', b)

"""
Filter a matrix so the only cells remaining are those divisible by 3 in rows that sum to 10 or higher.
"""
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output = []
#
# for row in matrix:
#     if sum(row) >= 10:
#         print(row)
#         for col in row:
#             if col % 3 == 0:
#                 output.append([col])
#     print(matrix)
#
# print('After filter operation', output)
#
# print('Using list comp', [[col for col in row if col % 3 == 0]
#                           for row in matrix if sum(row) >= 10])



