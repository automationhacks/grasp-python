import pickle
"""
    Purpose:
    Saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)
    sending python data over a TCP connection in a multi-core or distributed system (marshalling)
    storing python objects in a database
    converting an arbitrary python object to a string so that it can be used as a dictionary key (e.g. for caching & memoization).
"""

lst = ['Gaurav', 'Singh', 'is', 'a', 'Python', 'Developer']

file_name = 'pickle_demo_file'

with open(file_name, 'wb') as f1:
    pickle.dump(lst, f1)

with open(file_name, 'rb') as f2:
    lst2 = pickle.load(f2)

print(lst)
print(lst2)
print('Is obj 1 == obj 2? : ', lst == lst2)