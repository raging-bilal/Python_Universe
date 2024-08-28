# Method 2: By using comma operator

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("The number before swapping: ")
print("a: ",a)
print("b: ",b)

a,b=b,a

print("The number after swapping: ")
print("a: ",a)
print("b: ",b)


