the_list = [1, 2, 3]
the_iter = iter(the_list)
print(the_iter)

print('First', next(the_iter))
print('Second', the_iter.__next__())
print('Third', next(the_iter))
print('Fourth', the_iter.__next__())

