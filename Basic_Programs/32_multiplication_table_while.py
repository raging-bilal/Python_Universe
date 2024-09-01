def table(n):
    i=1
    while i<=10:
        pro=n*i

        print(n, " X ", i," = ", pro)
        i+=1

n=int(input("Enter the number to print the multiplication table: "))
table(n)