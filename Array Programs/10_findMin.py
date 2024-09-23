a=[32,455,6343,6,32,45,22]

print("Printing the original array! ")
for i in range(0,len(a)):
    print(a[i],end=" ")
    
print()



print("Printing the smallest array element! ")



min=a[0]
for i in range(0,len(a)):
    
    if a[i]<min:
        min=a[i]

print("The smallest value in the array : ",str(min))
