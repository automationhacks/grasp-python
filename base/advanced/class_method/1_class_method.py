"""
Creating class method using classmethod
"""


class Person:
    age = 25

    def print_age(cls):  # cls: class Person as an argument
        print('age ', cls.age)


Person.print_age = classmethod(Person.print_age)  # creating class method which can accept class as argument
print(Person.print_age)

Person.print_age()  # func call
