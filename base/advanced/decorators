
# Ex 1: Show Python functions are objects


# def first(msg):
#     print(msg)
#
# first('Hello')
#
# second = first
# second('Hello by Second')

# Ex 2: Higher order functions - Which can accept func as arguments

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operate(func, x):
#     return func(x)
#
# print(operate(inc, 5))
# print(operate(dec, 6))

# Ex 3: H.O.F can even return functions

# def is_called():
#
#     def is_returned():
#         print('Inside is_returned')
#     return is_returned
#
# new = is_called()  # Handle to returned func object
# new()  # Function call
# print(new)

"""
Theory:
    Functions and methods are called callable as they can be called
    In fact, any object which implements the special method __call__() is termed callable
    So, in the most basic sense, a decorator is a callable that returns a callable
    Basically, a decorator takes in a function, adds some functionality and returns it

    This is similar to packing a gift. The decorator acts as a wrapper.
    The nature of the object that got decorated (actual gift inside) does not alter.
    But now, it looks pretty (since it got decorated).
"""


# Ex 4: Basic Decorator example

# def make_pretty(func):
#
#     def inner():
#         print('I am decorated now')
#         func()
#     return inner
#
#
# def ordinary():
#     print('I am ordinary')
#
# # ordinary()
# pretty = make_pretty(ordinary)
# pretty()


# Ex 5: Syntactic sugar to implement decorators

# def prettifier(func):
#
#     def inner_func():
#         print('Additional functionality')
#         func()
#
#     return inner_func
#
# @prettifier
# def main_func():
#     print('Core Functionality')
#
# main_func() # Call for the func with additional func being decorated

# Ex 6: Decorating Functions with arguments

# Problem: Divide func which fails in case of Division by Zero error


# def divide(a, b):
#     return a / b
#
# print(divide(5, 2))
# print(divide(5, 0))

# Probable Solution:
# Note: Parameters of the nested inner() function inside the decorator,
# is same as the parameters of functions it decorates

# def smart_divide(func):
#
#     def inner(a, b):
#
#         print('Performing %s/%s' % (a, b))
#         if b == 0:
#             print('Cannot divide! Coming outside')
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def dumb_divide(a, b):
#     return a/b
#
# dumb_divide(5, 0)
# print(dumb_divide(5, 2))

# Ex 7: General Decorators
# args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments

# def generic_decorator(func):
#
#     def inner(*args, **kwargs):
#         print('Can decorate any function')
#         return func(*args, **kwargs)
#
#     return inner

# Ex 8: Chaining of Decorators in Python

def star(func):

    def inner(*args, **kwargs):

        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)

    return inner


def percent(func):

    def inner(*args, **kwargs):

        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)

    return inner

# With Syntactic sugar
# @star
# @percent
# def printer(msg):
#     print(msg)
#
# printer('Yo Chained!')

# Without Syntactic Sugar


def printer(msg):
    print(msg)

printer_obj = star(percent(printer))
printer_obj('Yo Chained without additional Sugar')



