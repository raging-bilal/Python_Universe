# Method 3: Using Dictionary Comprehension
# Python also provides a concise way to convert a list to a dictionary using dictionary comprehension. This method is particularly useful when you want to perform some operation on the elements of the list. Here's an example:

# List of fruits  
fruits = ['apple', 'banana', 'cherry']  
  
# Convert list to a dictionary using dictionary comprehension  
fruit_dict = {fruit: len(fruit) for fruit in fruits}  
  
print(fruit_dict)  