a1=[1,23,56,1,56,32,44,32,44,32]
f=[None] * len(a1)

visited=-1

for i in range(0,len(a1)):
    count=1

    for j in range(i+1,len(a1)):
        if(a1[i]==a1[j]):
            count=count+1
            f[j]=visited

    if(f[i]!=visited):
        f[i]=count


print("---------------------");    
print(" Element | Frequency");    
print("---------------------");    
for i in range(0, len(f)):    
    if(f[i] != visited):    
        print("    " + str(a1[i]) + "    |    " + str(f[i]));    
print("---------------------");  
