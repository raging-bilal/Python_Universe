# Python Program to Check if a Number is Odd or Even

def check(num):
    if(num%2==0):
        print("{0} is Even Number! ".format(num))

    else:
        print("{0} is Odd Number! ".format(num))


num=int(input("Enter the number to check even or odd: "))
check(num)
