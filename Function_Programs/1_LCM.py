def lcm(a,b):
    if a>b:
        greater=a

    else:
        greater=b


    while(True):
        if (greater%a==0) and (greater%b==0):
            lcm=greater
            break
        greater+=1

    print("The LCM of {0} and {1} is {2}! ".format(a,b,lcm))


a=int(input("Enter the first number to check the LCM: "))
b=int(input("Enter the second number to check the LCM: "))

lcm(a,b)



