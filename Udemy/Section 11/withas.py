"""
Section 11: File handling using "with" and "as" keywords

With / as keywords
"""

# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(my_read.read())

print("With as write start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as writing/reading.")

print()
print("With as read start")
with open("withas.txt", "r") as with_as_read:
    print(with_as_read.read())
