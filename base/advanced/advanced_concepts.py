
# concept: tuple of lists, allows modification of list elements using indexing
# atuple = ([1, 2, 3], [4, 5, 6])
# atuple[0][1] = 9
# print(atuple) # allowed
# atuple[0].append(8)
# print(atuple) # also allowed

# concept: if tuple has a mutable type, it can't be hashed
non_hashable_tuple = ([1, 2])
hashable_tuple = (1, 2)

print(hash(hashable_tuple)) # O/P 1299869600
print(hash(non_hashable_tuple))

# O/P 
# Traceback (most recent call last):
#   File ".\advanced_concepts.py", line 14, in <module>
#     print(hash(non_hashable_tuple))
# TypeError: unhashable type: 'list'
