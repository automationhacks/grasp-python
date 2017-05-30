import traceback

try:
    x, y = 5, 0
    print(x/y)
except:
    traceback.print_exc()