# Python program to swap two variables

# Method 1: By using Naïve Approach



a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("The number before swapping: ")
print("a: ",a)
print("b: ",b)

temp=a
a=b
b=temp

print("The number after swapping: ")
print("a: ",a)
print("b: ",b)
