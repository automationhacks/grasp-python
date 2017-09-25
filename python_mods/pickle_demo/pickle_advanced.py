import pickle
import os

class A:

    def __init__(self):
        self.a_int = 2
        self.a_str = 'Inside A'


    def pickle_it(self):
        path = os.path.dirname(__file__)
        pick_file = path + '//' + 'testpickle'
        print(pick_file)
        file_object = open(pick_file, 'wb')
        pickle.dump(self, file_object)
        file_object.close()

class B:
    def __init__(self):
        a_obj = A()
        a_obj.pickle_it()

        path = os.path.dirname(__file__)
        pick_file = path + '//' + 'testpickle'
        file_object = open(pick_file, 'rb')
        pick = pickle.load(file_object)
        print('b', pick, pick.a_int)
        self.b_int = 5
        self.b_str = 'Inside B'


if __name__ == '__main__':
    b = B()