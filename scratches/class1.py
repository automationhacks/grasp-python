
class Class1:
    def __init__(self):
        self.a = 'Gaurav'
        self.b = 5

    def print_hello(self):
        print(self.a)
        print(self.b)
        return 'Hello world Class 1'

class Class2:
    def __init__(self, c1_obj):
        self.x = c1_obj

    def print_type(self):
        print('From Class 2')
        print(self.x.a)
        print(self.x.b)

if __name__ == '__main__':
    c1_obj = Class1()
    c1_obj.print_hello()

    c2_obj = Class2(c1_obj)
    c2_obj.print_type()
