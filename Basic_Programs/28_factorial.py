
def Findfact(n):
   fact=1
   

   if n<0:
      print(n, " is negative number.So, its factorial doesnot exist!")
      

   elif n==0:
      print("The factorial of ",n," is 1!")

   else:
      
      for i in range(1,n+1):
         fact=fact*i
         print(fact)
   
n=int(input("Enter the number to find the factorial: "))

Findfact(n)
