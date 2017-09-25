"""
Theory:
    A function defined inside another function is called a nested function.
    Nested functions can access variables of the enclosing scope
    In Python, these non-local variables are read only by default,
    and we must declare them explicitly as non-local (using nonlocal keyword)
"""

# Ex 1: Nested func accessing non-local variable


# def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     printer()
#
# print_msg('Nested Demo')


# Ex 2: Function returning another function
"""
Theory:
    This value in the enclosing scope is remembered even when the variable goes out of scope
    or the function itself is removed from the current namespace
"""

# def print_msg(msg):
#     def printer():
#         print(msg)
#
#     return printer
#
# another_handle = print_msg('Yo is this a closure?')
# another_handle()  # Python closure: Data gets attached to code

"""
Theory:
    When do we have closure:
    We must have a nested function (function inside a function).
    The nested function must refer to a value defined in the enclosing function.
    The enclosing function must return the nested function.

    When to use?
    Closures can avoid the use of global values and provides some form of data hiding.
    It can also provide an object oriented solution to the problem when there is only few methods to be implemented
"""


# Ex 3: Sample use case for closure implementation


def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(9))
print(times5(10))

# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)
