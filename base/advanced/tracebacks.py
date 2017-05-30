import traceback

try:
    raise TypeError("Oups!")
except Exception as err:
    # str = traceback.print_tb(err.__traceback__)
    print(err)
