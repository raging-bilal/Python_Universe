def D2B(d):
    d1=int(d)
    b=bin(d1)
    print("The decimal value of {0} is equal to binary value of {1}! ".format(d1,b))

def D2O(d):
    d1=int(d)
    o=oct(d1)
    print("The decimal value of {0} is equal to octal value of {1}! ".format(d1,o))

def D2H(d):
    d1=int(d)
    h=hex(d1)
    print("The decimal value of {0} is equal to hexa value of {1}! ".format(d1,h))



d=int(input("Enter the number of DECIMAL NUMBER SYSTEM: "))

D2B(d)
D2O(d)
D2H(d)


