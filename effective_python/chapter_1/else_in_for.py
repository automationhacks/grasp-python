def else_in_for():
    for i in range(0, 3):
        print('loop %s' % i)
    else:
        print('In Else')  # Executed after for loop execution

    for i in range(0, 3):
        print('loop %s' % i)
        if i == 1:
            break
    else:
        print('In Else')  # Not called in case of break

"""
Find if 2 nos are co prime i.e. common divisor is 1
"""


def coprime():
    a = 4
    b = 9

    for i in range(2, min(a, b) + 1):
        print('Testing', i)
        if a % i == 0 and b % i == 0:
            print('Not co prime')
            break
    else:  # Avoid else in for as it is not explicit
        print('Co prime')

coprime()