a=[23,4,5,64,2,23,46,7,89,43]
l=len(a)
temp=0

print("Print the Original Array ! ")
for i in range(0,l):
    print(a[i], end=" ")

print()



for i in range(0,l):
    for j in range(i+1,l):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp



print("Print the elements of array in ascending order !")
for i in range(0,l):
    print(a[i], end=" ")





