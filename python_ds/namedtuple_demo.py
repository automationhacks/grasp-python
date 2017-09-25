from collections import namedtuple


Person = namedtuple('Person', 'name age gender')
print(type(Person))

bob = Person(name='Bob', age=30, gender='male')
print(type(bob))

jane = Person(name='Jane', age=28, gender='female')
print(type(jane))

for p in [bob, jane]:
    print('{} is a {} year old {}'.format(p.name, p.gender, p.age))