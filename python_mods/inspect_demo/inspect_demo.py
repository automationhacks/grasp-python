import inspect

class Foo():

    def foo(self):
        print('Get my name', foo1())
        print('Get my class name', self.__class__.__name__)


def foo1():
    stack = inspect.stack()
    the_class = stack[1][0].f_locals['self'].__class__.__name__
    the_method = stack[1][0].f_code.co_name

    return (the_class, the_method)

foo_obj = Foo()
foo_obj.foo()