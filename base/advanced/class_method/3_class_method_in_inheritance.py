"""
Usage 2:
class method can be used to correct instance creation in inheritance
"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name: %s age: %s' % (self.name, self.age))

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)  # return instance of child in an inheritance hierarchy

    @staticmethod
    def from_fathers_age(name, fathers_age, age_diff):
        return Person(name, date.today().year - fathers_age + age_diff)  # return instance of Person always


class Man(Person):
    sex = 'male'


# using class method
man = Man.from_birth_year('luke', 1985)
man.display()
print(isinstance(man, Man), type(man))

# using static method
father = Man.from_fathers_age('anakin', 1965, 20)  # Instance is always hard coded as Person
father.display()
print(isinstance(father, Man), type(father))
