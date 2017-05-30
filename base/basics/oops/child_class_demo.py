class Parent(object):
    def __init__(self):
        # for attr in self.ATTRS:
        #     setattr(self, attr, 0)

        print(self.ext_app)
        print(Child.ext_app)
        print(self.z)

        # print(setattr(self.ext_app))

        # print(self.ATTRS)
        # print(self.__dict__)

class Child(Parent):
    # #class variable
    # ATTRS = ['attr1', 'attr2', 'attr3']

    test_id = 'PVE-74380'
    test_url = 'http://jira/browse/PVE-74380'
    ext_app = 'Projectplace'
    category = 'Work'


    def __init__(self):
        self.z = 'Instance mem in child'
        super(Child, self).__init__()




c = Child()