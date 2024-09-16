# Python program to show how to use del keyword    
    
lst = ["Python", "Remove", "Elements", "List", "Tutorial", "Clear", "Pop", "Remove", "Delete"]    
print("The Initial list is ", lst)    
    
# Removing the first element of the list    
del lst[0]    
print("After removing the first element new list is", lst)    
    
# Removing the last element from the list    
del lst[-1]    
print("After removing the last element new list is", lst)    
    
# To remove the elements between a range    
del lst[:3]    
print("After removing element from index:5", lst)    
    
# Removing the last two elements from the list    
del lst[-2]    
print("After removing the last 2 elements from the list", lst)    
    
# Removing the elements between a range having the start and stop indices    
del lst[1:5]    
print("After removing elements present in the range 1:5", lst)   