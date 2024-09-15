# Method 2: Using zip()
# Another method to convert a list to a dictionary is by using the zip() function. This function pairs elements from multiple iterables, such as lists, together. Here's an example:

# List of fruits and their prices  
fruits = ['apple', 'banana', 'cherry']  
prices = [1.00, 0.50, 1.50]  
  
# Convert lists to a dictionary using zip()  
fruit_dict = dict(zip(fruits, prices))  
  
print(fruit_dict)  