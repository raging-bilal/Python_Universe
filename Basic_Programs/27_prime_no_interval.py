def checkPrimeInRange(l,u):
    for i in range(l,u+1):
        if i >1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)


l=int(input("Enter the lower limit: "))
u=int(input("Enter the upper limit: "))

checkPrimeInRange(l,u)




