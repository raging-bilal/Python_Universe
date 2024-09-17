# Removing Elements from Dictionary
# Using the pop() function, we can eliminate a specific item from a dictionary. This function returns the value of the key removed.

# The popitem() function removes and returns any (key, value) element pair from the given dictionary. We can use the clear() function to erase all objects in one go.

# We could also use the del keyword to eliminate single items or even the entire dictionary.

# Code

# Program to show how to remove elements from a dictionary  
  
# initializing a dictionary  
Dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}  
  
# removing a key:value pair from the dictionary using pop()  
Dictionary.pop(4)  
print("\nAfter removing a key using pop(): ")  
print(Dictionary)  
  
# remove any item at random using popitem()  
Dictionary.popitem()  
print("\nAfter removing an arbitrary key: ")  
print(Dictionary)  
  
# remove all the items present in dictionary  
print("\nAfter removing all the items: ")  
Dictionary.clear()  
print(Dictionary)  
  
# deleting the dictionary variable  
del Dictionary  
  
# Printing dictionary after deleting it  
try:  
    print(Dictionary)  
except:  
    print('No dictionary of the given name')  