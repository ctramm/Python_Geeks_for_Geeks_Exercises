# Python program for escape sequencing of string

# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String2 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String2)

# Escaping Double Quotes
String3 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String3)

# Printing paths with the use of Escape Sequences
String4 = "C:\\Python\\Geeks\\"
print("\nEscaping backslashes: ")
print(String4)

# Using raw string to ignore escape sequences
String5 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String5)

