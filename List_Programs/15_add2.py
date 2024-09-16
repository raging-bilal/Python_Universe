# Let's consider a program to add the two list in Python using the Naïve Method.

# comprehension.py

# initialize the Python lists  
lt1 = [2, 4, 6, 8, 10, 30]  
lt2 = [2, 4, 6, 8, 10, 12]  
  
# print the original list element  
print ( " Python list 1 : " + str (lt1))  
print ( "Python list 2 : " + str (lt2))  
  
# use list comprehension to add two lists.  
res_lt = [ lt1[x] + lt2[x] for x in range (len (lt1))]  
  
  
# Display the sum of two list in Python  
print ( " Addition of the list lt1 and lt2 is: " + str (res_lt))     