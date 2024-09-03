def hcf(a,b):
    if a<b:
        smaller=a

    else:
        smaller=b

    for i in range(1,smaller+1):
        if ((a%i==0) and (b%i==0)):
            hcf=i

    

    print("The HCF of {0} and {1} is {2}! ".format(a,b,hcf))

a=int(input("Enter the first number to check the HCF: "))
b=int(input("Enter the second number to check the HCF: "))

hcf(a,b)
