# # Default function to implement conditions to check leap year  



def checkLeap(y):
    if (y%400==0)  or ((y%4==0) and (y%100!=0)):
        print("{0} is the Leap year! ".format(y))



    else:
        print("{0} is NOT the Leap year! ".format(y))


y=int(input("Enter the year to check for leap Year: "))

checkLeap(y)
