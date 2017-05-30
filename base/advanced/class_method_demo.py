import sys

class Demo:
    message = 'Çlass Member'
    def __init__(self):
        self.message1 = 'Instance member'

    @classmethod
    def cMethod(cls):
        print(cls.message)

    def iMethod(self):
        print(self.message)

    @staticmethod
    def sMethod():
        message = 'Static M'
        print(message)

if __name__ == '__main__':
    # Demo.cMethod()
    demo_obj = Demo()
    demo_obj2 = Demo()
    # demo_obj.cMethod()
    #
    # Demo.sMethod()
    # demo_obj.sMethod()
    #
    # Demo.iMethod(demo_obj)

    print(demo_obj.message)
    print(demo_obj2.message)


