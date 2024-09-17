# Adding Elements to a Dictionary
# The insertion of items in the Python Dictionary could be done in various methods. Items can be added to the dictionary using this particular format Dictionary[Key] = 'Value'. We can use the in-built update() function to update a current key in a Dictionary. Nested key: values can also be inserted into a preexisting Dictionary. If the key-value combination is present in the dictionary, the value for that key is modified; if this is not the case, a new key is created and added to the Dictionary with the given value.

# Code

# Initializing an empty Dictionary  
Dictionary = {}  
print("The empty Dictionary: ")  
print(Dictionary)  
   
# Inserting key:value pairs one at a time  
Dictionary[0] = 'Javatpoint'  
Dictionary[2] = 'Python'  
Dictionary.update({ 3 : 'Dictionary'})  
print("\nDictionary after addition of these elements: ")  
print(Dictionary)  
   
# Adding a list of values to a single key  
Dictionary['list_values'] = 3, 4, 6  
print("\nDictionary after addition of the list: ")  
print(Dictionary)  
   
# Updating values of an already existing Key  
Dictionary[2] = 'Tutorial'  
print("\nUpdated dictionary: ")  
# print(Dict)  
   
# Adding a nested Key to our dictionary  
Dictionary[5] = {'Nested_key' :{1 : 'Nested', 2 : 'Key'}}  
print("\nAfter addtion of a Nested Key: ")  
print(Dictionary)