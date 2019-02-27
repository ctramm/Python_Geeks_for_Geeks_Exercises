"""
Section 5: Boolean Operators - Order of Operations (Precedence)

1. not
2. and
3. or
"""

output = True or not False and False
# not False = True
# Not False = True
# True or False = True
print(output) # True result

obj = 10 == 10 or not 10 > 10 and 10 > 10
# True or not False and False
print(obj) # True result

stuff = (10 == 10 or not 10 > 10) and 10 > 10
# (True or True) -> (True) and False --> False
print(stuff) # False result
