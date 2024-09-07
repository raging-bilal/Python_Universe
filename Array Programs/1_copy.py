a1=[1,2,334,56,78]
a2=[None]*len(a1)

for i in range(0,len(a1)):
    a2[i]=a1[i]

print("The elements of array 1 are as followS: ")
for i in range(0,len(a1)):
    print(a1[i])

print("The elements of array 1 are as followS: ")
for i in range(0,len(a2)): 
    print(a2[i])


