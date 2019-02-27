"""
Examples to show available string methods in python
"""

# Replace Method
b = "1abc2abc3abc4abc"
print(b.replace('abc', 'ABC'))

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = b[1:6]
step = b[1:6:2]

print("****************")

print(sub)
print(step)