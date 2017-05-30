import os
import sys
import traceback

# path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', ''))
# sys.path.extend([path])

import controller

try:
    # controller.flaky_func()
    controller.flaky_func1()
except Exception as e:
    # print(sys.exc_info())

    print(traceback.format_exc())
    # print('Logging global exception %s' % sys.exc_info())
finally:
    print('Inside finally block of main')