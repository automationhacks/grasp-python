class Parent(object):
    def implicit(self):
        print('parents implicit')

    def override(self):
        print('parents override')

    def altered(self):
        print('parents altered')


class Child(Parent):
    def override(self):
        print('Child override')

    def altered(self):
        print('Child, before parent altered()')
        super(Child, self).altered()
        print('Child, after parent altered()')


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
