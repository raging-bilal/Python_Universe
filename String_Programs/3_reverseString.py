# Python Program to reverse a string


def reversefunction(string):
    reverse_string=""
    l=len(string)



    if not string:
        return "Empty String! Please enter the string."
    


    # By For Loop----------------------------------
    
    for i in range(l-1,-1,-1):
    
        reverse_string +=string[i]
    return reverse_string

    

    # By slicing-----------------------------------  
    # reverse_string=string[::-1]

    # return reverse_string



string=input("Enter the string to reverse: ")
result=reversefunction(string)
print(result)








