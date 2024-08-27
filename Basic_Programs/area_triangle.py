# This is to find the area of any triangle 

a=float(input("Enter the length of first side: "))

b=float(input("Enter the length of second side: "))

c=float(input("Enter the length of third side: "))

s= (a+b+c)/2
print("The value of s is: ", str(s))

area=(s*(s-a)*(s-b)*(s-c)) **0.5

print('The area of the triangle is %0.2f' %area)
