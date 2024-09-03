import calendar as c

def calc(yy,mm):

    r=c.month(yy,mm)

    print(r)

yy=int(input("Enter the Year: "))
mm=int(input("Enter the month: "))

calc(yy,mm)