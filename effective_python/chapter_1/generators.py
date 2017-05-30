"""
read a file and return the number of characters on each line
"""

print([len(line) for line in open('input.txt', 'r')])

iterable = (len(line) for line in open('input.txt', 'r'))  # Generator expression
print(iterable, type(iterable))
print(next(iterable), next(iterable))

root = ((x, x * 0.5) for x in iterable)
print(root, next(root), next(root))
