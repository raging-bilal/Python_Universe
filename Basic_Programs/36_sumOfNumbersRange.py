def sum(a,b):
    if a<=0 or b<=0:
        print("INVALID INPUT! Enter the natural number!")

    else:


        sum=0
        for i in range(a,b+1):

            sum=sum+i
        print("The sum of numbers range from {0} to {1} is {2}.".format(a,b,sum))


a=int(input("Enter the first number to calculate sum: "))
b=int(input("Enter the last number to calculate sum: "))

sum(a,b)