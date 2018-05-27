# alist = [0, 1, 2, 3]
# print(alist[0])
# print(list.__getitem__(alist, 2))

# adict = {'a': 1, 'b':2}
# print(adict['a'])
# print(dict.__getitem__(adict, 'b'))

# What is mro? - http://python-history.blogspot.in/2010/06/method-resolution-order.html
# Few more blogs on duck typing:
# https://hackernoon.com/python-duck-typing-or-automatic-interfaces-73988ec9037f
# https://ericlippert.com/2014/01/02/what-is-duck-typing/
# http://www.voidspace.org.uk/python/articles/duck_typing.shtml

class Duck:
    def quack(self):
        print("Quacked")

class AnotherDuck:
    def quack(self):
        print("Louder Quack")

class Eagle:
    def fly(self):
        print("Dude i just fly")

class MakeItQuack:
    def __init__(self, bird):
        bird.quack()

MakeItQuack(Duck())
MakeItQuack(AnotherDuck())
MakeItQuack(Eagle())