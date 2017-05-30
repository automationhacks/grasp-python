list_digits = list(range(5))
print(list_digits)

num = int(input('Enter a no\n'))

for i in list_digits:
    if num == i:
        print('no found')
        break
    else:
        print('no not found')
