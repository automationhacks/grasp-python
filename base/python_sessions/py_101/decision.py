a = 10
b = [5, 10, 20]

if a in b:
    print('element found in list')
    if a <= sum(b):
        print('a is less than or equal to sum of elements in b')
    else:
        print('a is more than sum of elements in b')
elif b:
    print('Valid list')
else:
    print('a not in b')



