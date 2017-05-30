names = ['Gaurav', 'Juhi', 'Sanchit', 'Siddharth']
letters = [len(name) for name in names]

print(names, letters)

"""
Use zip to process iterators in parallel
In Python 3, zip is a lazy generator that produces tuples.
In Python 2, zip returns the full result as a list of tuples
"""

count = 0
max_letters = 0
longest_name = ''

for name, letters in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name, max_letters)