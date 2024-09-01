n=int(input("Enter the positive integer to get the Fibonacci series: "))

n1=0
n2=1

count=0

if n<=0:
    print("ERROR:INVALID INPUT! Please enter positive integer.")

elif n==1:
    print(str(n1))

else:
    print(n1)
    while count<n:
        nth=n1+n2
        
        n1=n2
        n2=nth
        nth=n1

        
        print(nth)
        count+=1

        