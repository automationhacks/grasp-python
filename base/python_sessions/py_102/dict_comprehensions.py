keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {}

# Using For
for key, val in zip(keys, values):
    d[key] = val
print('Using For', d)

# Using Dict Comprehension
d1 = {key: val for key, val in zip(keys, values)}
print('Using Dict Comprehension', d1)
