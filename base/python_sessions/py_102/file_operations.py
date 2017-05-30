# f = open('test.txt', 'w')  # Write in text mode
# f = open('test.txt')  # Default mode is r
#
# f = open('img.bmp', 'w+b')  # write in binary mode
# f = open('img.bmp', 'r+b')  # read and write in binary mode
#
# # Specify encoding since windows default encoding
# # is cp1252 and in linux its utf-8
# f = open('test.txt', mode='r', encoding='utf-8')
# f.close()
#
# try:
#     f = open('test.txt', mode='r', encoding='utf-8')
# finally:
#     f.close()
#
# with open('test.txt', mode='w', encoding='utf-8') as f:
#     pass

# with open('text.txt', mode='w', encoding='utf-8') as f:
#     f.write('first line\n')
#     f.write('second line\n')
#     f.write('third line\n')

with open('text.txt', mode='r', encoding='utf-8') as f:
    print(f.read(5))  # Reads first 5 characters in file
    print(f.read())  # Reads entire file




