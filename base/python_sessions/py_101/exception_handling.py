x, y = 5, 0

try:
    z = x / y
except ZeroDivisionError as e:
    print('Exception encountered ', e)
finally:
    print('All done')
