# func firstn to represent all non negative nos till n


def firstn(n):
    return [num for num in range(n)]


print(firstn(20))


class FirstN(object):
    def __init__(self, n):
        self.n, self.num, self.nums = n, 0, []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()


sum_of_first_n = sum(FirstN(10))
print(sum_of_first_n)
