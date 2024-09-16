# Let's consider a program to add the two list in Python using the Naïve Method.

# naivePro.py

# initialize the Python lists  
lt1 = [5, 10, 15, 20, 25, 30]  
lt2 = [2, 4, 6, 8, 10, 12]  
  
# print the original list element  
print ( " Python Original list 1: " + str (lt1))  
print ( "Python Original list 2: " + str (lt2))  
  
# use naive method to add two list.  
res_lt = [] # declaration of the list  
for x in range (0, len (lt1)):  
    res_lt.append( lt1[x] + lt2[x])  
  
# Display the sum of two list in Python  
print ( " Addition of the list lt1 and lt2 is: " + str (res_lt))  