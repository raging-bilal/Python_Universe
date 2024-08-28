# Method 4: By using arithmetic operators

# In this method, we can swap values of both the variable in two ways:
# Using addition and Subtraction operator:


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("The number before swapping: ")
print("a: ",a)
print("b: ",b)

a= a+b
b= a-b
a= a-b

print("The number after swapping: ")
print("a: ",a)
print("b: ",b)

