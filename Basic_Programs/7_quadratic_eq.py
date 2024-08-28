import cmath

a=int(input("Enter the value of a in ax^2 + bx + c : "))

b=int(input("Enter the value of b in ax^2 + bx + c : "))

c=int(input("Enter the value of c in ax^2 + bx + c : "))

d1= (-b + cmath.sqrt(b**2 - 4 * a * c)) / 2 * a

d2= (-b - cmath.sqrt(b**2 - 4 * a * c)) / 2 * a

print("The roots are {0} and {1}".format(d1,d2))

