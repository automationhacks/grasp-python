# generator which yields items instead of returning a list


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(firstn(10))
print(sum(firstn(10)))
