# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[1] = 'For'
Dict[2] = 'Geeks'
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values to a single key
Dict['Value_Set'] = 2, 3, 4
print("\nDictionary after adding 3 elements to a single key: ")
print(Dict)

# Updating existing key's value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding nested key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
