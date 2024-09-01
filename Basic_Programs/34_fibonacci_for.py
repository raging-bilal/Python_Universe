n=int(input("Enter the positive number: "))

a=0
b=1

for i in range(0,n):
    print(a)
    nth=a+b
    a=b
    b=nth
    