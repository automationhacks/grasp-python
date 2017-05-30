import traceback
import sys


def func():
    res = 5 /0


try:
    func()
except Exception as e:
    # print(traceback.print_exc())
    # print(sys.exc_info())
    # # print()
    # print(type(sys.exc_info()[1]))
    print(traceback.print_tb(sys.exc_info()[2]))

    # print(str(e))
    # print(sys.exc_info()[0])

