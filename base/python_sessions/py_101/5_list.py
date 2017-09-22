# empty list
my_list = []

# list of integers
list_int = [1, 2, 3]
# list with mixed data types
list_mixed = [1, "Hello", 3.4]
# nested list
list_nested = ["mouse", [8, 4, 6]]

print(list_int[-1])
print(list_mixed[1:2])  # [x:y] here y is not included and x and y are both indexes
print(list_nested[1][0:2])

list_orig = [1, 2]
list_orig[1] = 3
print(list_orig)
