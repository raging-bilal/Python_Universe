# 2. Using join() Method and map() Method




# map(function, iterable)    


# Python program to convert a list to a string by using the join() method and map method  
  
# Creating a list with some elements of int data type  
iterable = ["Python", "Convert", 11, "List", 12, "String", "Method"]  
  
# Converting to string  
string = " ".join (map (str, iterable))  
  
  
# Printing the string  
print (string)  
print (type(string))  
