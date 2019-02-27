"""
Section 5: Understanding Boolean Operators

and
***********************************
True and True       --> True
True and False      --> False
False and False     --> True
***********************************

or
***********************************
True or True        --> True
True or False       --> True
False or False      --> False
***********************************

not
***********************************
Not True        --> False
Not False       --> True
***********************************
"""

print("Examples of 'and' operators")
and_output1 = (10 == 10) and (10 > 9)
print(and_output1)

and_output2 = (10 == 10) and (10 < 9)
print(and_output2)

and_output3 = (10 > 10) and (10 < 9)
print(and_output3)

print("\nExamples of 'or' operators")
or_output1 = (10 == 10) or (10 > 9)
print(or_output1)

or_output2 = (10 == 10) or (10 < 9)
print(or_output2)

or_output3 = (10 > 10) or (10 < 9)
print(or_output3)

print("\nExamples of 'not' operators")
not_true = not (10 == 10)
print(not_true)

not_false = not (10 != 10)
print(not_false)

