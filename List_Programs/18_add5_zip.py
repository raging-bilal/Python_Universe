# Let's consider a program to add the list elements using the zip function and sum function in Python.

# zipSum.py

# initializing of the lists lt1 and lt2  
lt1 = [6, 12, 18, 3, 6, 9]  
lt2 = [4, 8, 12, 2, 4, 6]  
  
# display the original items of the lists lt1 and lt2  
print ("Display the elements of List 1 " + str(lt1))  
print ("Display the elements of List 2 " + str(lt2))  
  
# use the zip() function and sum() function to group the lists add the lists' lt1 and lt2 with index #wise.   
result_lt = [sum(i) for i in zip(lt1, lt2 )]  
  
# Display the sum of the two list  
print (" Sum of the list 1 and list 2 is : " + str(result_lt))  
