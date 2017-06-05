"""
Usage1:
class method can be used to create factory method which returns a class object for diff use cases

"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age_from_birth_year = date.today().year - birth_year
        return cls(name, age_from_birth_year)  # returns instance of Person with different age

    def display(self):
        print('Name: %s Age: %s' % (self.name, str(self.age)))


person = Person('gaurav', '28')  # uses __init__
person.display()

another_person = Person.from_birth_year('sam', 1985)  # using class method
another_person.display()
