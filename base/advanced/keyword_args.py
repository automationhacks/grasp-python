import sys

class Demo:

    def __init__(self, **kwargs):

        print(kwargs)
        if kwargs:
            self.name = kwargs['name']
            print(self.name)

        print('Normal cond')



if __name__ == '__main__':
    args = sys.argv
    name = 'Gaurav'
    env = 'PVE'

    dem = Demo(name=name, env=env)
    dem1 = Demo()
