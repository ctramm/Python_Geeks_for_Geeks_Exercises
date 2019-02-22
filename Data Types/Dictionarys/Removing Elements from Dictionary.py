# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a key from nested dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a key using pop()
Dict.popitem()
print("\nPops first element: ")
print(Dict)

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting entire Dictionary: ")
print(Dict)
