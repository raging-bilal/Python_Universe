# concatenate two strings in Python

# 1. Using + Operator:------------------------------------------------------

# Two string concatenation using Python program  
# Initialisation of two strings    
str1 = "Hello "    
str2 = "Coders"    
 # Using + Operator, we add two strings in strings concatenation    
str3 = str1 + str2    
  # Printing the new string, which is combination of str1 and str2  
print("The new combined string is:",str3)     




# 2. Using join() method------------------------------------------------------------

# Two string concatenation using Python program  
# Initialisation of two strings      
str1 = "Hello"    
str2 = "JavaTpoint"    
# join() method is used to combine the strings    
print("".join([str1, str2]))    
# join() method is used to combine    
# the string with a separator Space(" ")    
str3 = " ".join([str1, str2])    
print("The new combined string is:",str3)    






# 3. Using % Operator-------------------------------------------------------------------

# Three string concatenation using Python program  
# Initialisation of three strings      
str1 = "Hello"    
str2 = "coders"    
str3 = "India"  
# % Operator is used here to combine the string    
print("% s % s %s" % (str1, str2, str3))  









# 4. Using format() function---------------------------------------------------------------------

# Three string concatenation using Python program  
# Taking user inputs of three strings      
str1 = input("Enter the value of Str1: ")   
str2 = input("Enter the value of Str2: ")  
str3 = input("Enter the value of Str3: ")  
# format function is used here to concatenate the strings     
print("{} {} {}".format(str1, str2, str3))     
# Store the result in new variable, str4  
str4 = "{} {} {}".format(str1, str2, str3)     
 # Print the combined string which is stored in str4  
print(str4)   