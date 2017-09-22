def args_demo(p_arg, *argv):
    print('Positional args: ', p_arg)
    for arg in argv:
        print('Variable argument: ', arg)


args_demo('Iron Man', 'Captain America', 'Hulk', 'Black Widow')


def greet(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('%s == %s' % (key, value))


greet(name='Jack Robins', age='25', height='5.11')
