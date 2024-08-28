# Method 3: By using XOR method

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("The number before swapping: ")
print("a: ",a)
print("b: ",b)

a= a^b
b= a^b
a= a^b

print("The number after swapping: ")
print("a: ",a)
print("b: ",b)


