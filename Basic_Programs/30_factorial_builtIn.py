import math as m

def fact(n):
    if n>=0:
        f=m.factorial(n)
        print(f)

    else:
        print("ERROR: INVALID INPUT!")


n=int(input("Enter the number to find the factorial using builtin functions: "))

fact(n)
