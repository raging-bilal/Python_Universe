def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i

    print("The sum of first {0} natural numbers is {1}".format(n,sum))


n=int(input("Enter the number till you want to calculate the sum: "))
sum(n)
