a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[:4])
print(a[-4:])
print(a[3:-2])
# Start - inclusive, end - exclusive

""" Example of stride in slicing :: """
fruits = ['banana', 'orange', 'apple', 'strawberry', 'mango', 'grapes']
print('Odds ', fruits[1::2])
print('Evens ', fruits[::2])

x = b'mongoose'
y = x[::-1]
print(y)

w = '謝謝'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')