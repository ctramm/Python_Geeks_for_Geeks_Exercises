"""
table
object reference count
"""

b = "nyc"
b = "nyc"

print(b)

b = 123

print(b)
print(b)

b = 456
print(b)

c = 'nyc'
d = c

print(c == d)
print(d is c)
