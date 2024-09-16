# Let's consider a program to take the input list element from the user and add them.

# Accept.py

# Declaration of the lt1, lt 2 and lt3 lists  
lt1 = []  
lt2 = []  
lt3 = []  
  
# Takes a numeric number from the user to define the total size of the list  
items = int (input (" Enter the total number of the list elements: "))  
  
# Enter the list elements from the user one by one.  
print (" Enter the items into List 1 : ")  
for i in range(1, items + 1):  
    num = int ( input (" Enter the value of %d index is :" %i))  
    lt1.append(num) # insert the items into the list1  
  
# Enter the list elements from the user one by one.  
print (" Enter the items into the List 2 : ")  
for i in range(1, items + 1):  
    num = int ( input (" Enter the value of %d index is :" %i))  
    lt2.append(num) # insert the items into the list2  
      
for j in range(items):  
    lt3.append (lt1[j] + lt2[j]) # add the list items of both list lt1 and lt2 into the lt3     
print ("\n Addition of the two lists is ", lt3)  