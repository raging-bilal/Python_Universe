# A default function for Prime checking conditions  


def checkPrime(p):
    if p>1:
        for i in range(2, int(p/2) +1):
            if p%i==0:
                print("{0} is NOT Prime Number !".format(p))
                break          
        else:   
            print("{0} is Prime Number !".format(p))

    else:
        print("{0} is NOT Prime Number !".format(p))


p=int(input("Enter the number to check for the PRIME: "))

checkPrime(p)
