a=[1,2,3,4,5,6,7,8,9]

print("Printing the original array! ")
for i in range(0,len(a)):
    print(a[i],end=" ")
    
print()

print("Printing the array in reverse order! ")
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")