# Python program for Formatting of Strings

# Default Order
String = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String2 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
print("\nPrint String in order of Keywords: ")
print(String2)

# Formatting of Integers
String3 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String3)

# Formatting of Floats
String4 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String4)

# Rounding off Integers
String5 = "{0:.2f}".format(1/6)
print("\n The decimal of one-sixth is :")
print(String5)

# String alignment
String6 = "|{:<10}|{:^10}|{:>10}|".format("Geeks", "for", "Geeks")
print("\nLeft, center and right alignment with Formatting: ")
print(String6)


