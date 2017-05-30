import sys, os


path = os.path.join(os.path.dirname(__file__), '..')
print(path)
sys.path.extend([path])

print(len(sys.path))
print(sys.path[-1])

from dir1.dir_inside_1 import mod_inside_dir1 as util

util.here()

