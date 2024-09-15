# Method 1: Using a Loop
# One of the simplest ways to convert a list to a dictionary is by using a loop. This method allows you to specify the keys and values explicitly. Here's an example:

# List of fruits  
fruits = ['apple', 'banana', 'cherry']  
  
# Initialize an empty dictionary  
fruit_dict = {}  
  
# Populate the dictionary using a loop  
for idx, fruit in enumerate(fruits):  
    fruit_dict[idx] = fruit  
  
print(fruit_dict) 