"""
Section 11: How to write data to a file

File I/O
'w' -> Write-Only mode
'r' -> Read-only mode
'r+' -> Read and Write Mode
'a' -> Append mode
"""

my_list = [1, 2, 3]

my_file = open("firstfile.txt", 'w')

for item in my_list:
    my_file.write("This is item: " + str(item) + "\n")


my_file.close()
