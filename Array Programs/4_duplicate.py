a=[1,2,3,4,2,3,5,6,4]

print("Printing the duplicate elements in the array: ")

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            print(a[j])