import cmath

def find_roots(a,b,c):

    d=b**2-4*a*c

    sq_d=cmath.sqrt(d)

    x1= (-b+sq_d) / 2*a
    x2= (-b-sq_d) / 2*a




    if d>0:
        print("Real and distinct roots!")

        print("Root 1: ",x1 )
        print("Root 2: ",x2)

    elif d==0:
        print("Real and same roots!")

        print("Root 1: ",x1 )
        print("Root 2: ",x2)

    else:
        print("Imaginary roots!")

        print("Root 1: ",x1 )
        print("Root 2: ",x2)




a=int(input("Enter the value of a in ax^2 + bx + c: "))

b=int(input("Enter the value of b in ax^2 + bx + c: "))

c=int(input("Enter the value of c in ax^2 + bx + c: "))


find_roots(a,b,c)

