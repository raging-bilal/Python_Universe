def rec_fib(n):
    if n<=1:
        return n

 
    else:
        return (rec_fib(n-1)+rec_fib(n-2))
    
n=int(input("Enter the number till you want to print fabonacci series: "))
if n<=0:
    print("INVALID INPUT!")
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(rec_fib(i)) 