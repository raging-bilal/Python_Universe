def table(n):
    for i in range(1,11):
        r=n*i
        print(n, " X ", i, " = ",r )

n=int(input("Enter the number whose multiplication table should be printed: "))
table(n)