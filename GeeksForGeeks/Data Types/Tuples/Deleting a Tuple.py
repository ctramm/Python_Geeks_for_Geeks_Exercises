"""
Tuples are immutable and hence they do not allow deletion of a part of it.
Entire tuple gets deleted by the use of del() method.
Note - Printing of Tuple after deletion results in error.
"""

# Deleting a Tuple
Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)
