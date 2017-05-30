from collections import deque

d = deque()

d.append('1')
d.append('2')
d.appendleft('3')

print(d)

d.pop()
d.popleft()

print(d)

d1 = deque(maxlen=5)

d1.append('1')
d1.append('2')
d1.append('3')
d1.append('4')
d1.append('5')
d1.append('6')

print(d1)

d2 = deque()
d2.extend([1, 2, 3])
d2.extendleft([4, 5, 6])

print(d2)
