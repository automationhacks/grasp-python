class Sample:

    id = 'PVE-74378'

    def __init__(self):
        # self.zid = Sample.zid
        print('Inside __init__')
        print('Instance mem: %s' % (self.id))

class Sample1:

    def __init__(self, obj):
        self.x = obj
        print(self.x.id)



if __name__ == '__main__':
    print('Inside main block')
    # print('Class mem from main block', Sample.zid)
    s = Sample()
    b = Sample1(s)
    print('Program done')