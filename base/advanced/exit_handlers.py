import atexit


def all_done():
    print('All done')


def my_cleanup(name):
    print('my_cleanup(%s)' % name)

print('Registering')
atexit.register(all_done)
print('Registered')

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')

