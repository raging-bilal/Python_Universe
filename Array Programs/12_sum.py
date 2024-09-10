a=[1,2,3,4,5,6,7,8,9,10]
l=len(a)
for i in range(0,l):
    print(a[i], end=" ")

print()
sum=0
for i in range(0,l):
    sum=sum+a[i]

print("The sum of the elements of above array is {0} !".format(sum))



