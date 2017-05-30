import os

# with open('Sample.txt', 'w') as f:
#     f.write(os.urandom(10)) # TypeError: write() argument must be str, not bytes in Py3

with open('Sample.txt', 'wb') as f:
    f.write(os.urandom(10)) # for read use rb instead of r