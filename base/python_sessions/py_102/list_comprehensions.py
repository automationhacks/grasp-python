# # Find square of numbers in a list
#
# # Using For Loop
# numbers = list(range(15))
# squared, temp = [], 0
#
# for num in numbers:
#     temp = num ** 2
#     squared.append(temp)
#
# print('Using For', squared)
#
# # Using List Comprehension
# output = [num ** 2 for num in numbers]
# print('Using List Comprehension', output)

# Find square of numbers in a list if number is divisible by 2

# Using For Loop
numbers = list(range(15))
squared, temp = [], 0

for num in numbers:
    if num % 2 == 0:
        temp = num ** 2
        squared.append(temp)

print('Using For', squared)

# Using List Comprehension
output = [num ** 2 for num in numbers if num % 2 == 0]
print('Using List Comprehension', output)

