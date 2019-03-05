"""
Section 11: How to read a file

File I/O
Reading a file -> .read()
Reading line by line -> .readline()
"""

my_file = open('firstfile.txt', 'r')

print(my_file.read())

my_file.close()

print("Line by line ======>")

my_file_line = open('firstfile.txt', 'r')
print(my_file_line.readline())
print(my_file_line.readline())
print(my_file_line.readline())

my_file_line.close()
