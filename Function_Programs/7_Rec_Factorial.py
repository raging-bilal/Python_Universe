def rec_fac(n):
    if n==1:
        return n
    
    else:
        return n* rec_fac(n-1)



n=int(input("Enter the number to calculate its factorial: "))

if n<0:
    print("INVALID INPUT!")

elif n==0:
    print(1)

else:
    print("The factorial of {0} is {1} !".format(n,rec_fac(n)))