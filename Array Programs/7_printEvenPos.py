a=[1,2,3,4,5,6,7,8,9]

print("Printing the original array! ")
for i in range(0,len(a)):
    print(a[i],end=" ")
    
print()

print("Printing the array elements from even position only! ")
for i in range(1,len(a),2):
    print(a[i],end=" ")