# Python Program to check if a Number is Positive, Negative or Zero


def checkno(num):
    if num>0:
        print("{0} is postive number !".format(num))

    elif num<0:
        print("{0} is negative number !".format(num))

    else:
        print("{0} is Zero !".format(num))



num=int(input("Enter the number: "))

checkno(num)

