a=[1,2,3,34,32,455,6343,6,32,45,22]

print("Printing the original array! ")
for i in range(0,len(a)):
    print(a[i],end=" ")
    
print()

print("Printing the largest array element! ")



max=a[0]
for i in range(0,len(a)):
    
    if a[i]>max:
        max=a[i]

print("The largest value in the array : ",str(max))