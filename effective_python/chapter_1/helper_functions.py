"""
Parse a query string given as a string argument (data of type application/x-www-form-urlencoded). Data are returned as a dictionary.
The dictionary keys are the unique query variable names and the values are lists of values for each name.
"""

from urllib.parse import parse_qs

values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(values))

"""
official Python documentation says __repr__ is used to compute the “official” string representation of an object
and __str__ is used to compute the “informal” string representation of an object
"""

print('red %s' % values.get('red'))
print('blue %s' % values.get('blue'))
print('green %s' % values.get('green'))

red = int(values.get('red', [''])[0] or 0)
blue = int(values.get('blue', [''])[0] or 0)
green = int(values.get('green', [''])[0] or 0)

print('red %r' % red)
print('blue %r' % blue)
print('green %r' % green)

"""
    Helper function for above logic can be
"""

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found