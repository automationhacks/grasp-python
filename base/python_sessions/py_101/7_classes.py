class Hello:
    a = 10

    """ Hello classes Docstring """

    def __init__(self, mem):
        print('Inside the constructor')
        self.mem = mem

    def func(self):
        print(self.mem)
        print('Hello')

    @staticmethod
    def func_1(self):
        print('Hello again')


print('Accessing class member ', Hello.a)
print('Func memory address ', Hello.func)
print('Get Docstring using __doc__ ', Hello.__doc__)
print('Accessing func method')
hello_obj = Hello(10)
hello_obj.func()
