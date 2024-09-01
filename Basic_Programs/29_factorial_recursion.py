def fact(n):

    if(n>=0):
        if n==0 or n==1:

            return 1
    
        else:
            return n*fact(n-1)
        
    else:
        print(n, " is a negative number. It is an invalid Input!")

    
    
        
    
n=int(input("Enter the number to find the factorial: "))
f=fact(n)
print(f)
            
