n,v=[int(x) for x in input().split()] 
i=1
b=[]
sum1=0
while(i<=n):
    arr=[int(x) for x in input().split()]
    flag=False
    for j in range(1,arr[0]+1):
        if arr[j]<v:
            flag=True
            
    if(flag):
        sum1=sum1+1
        b.append(i)
    i=i+1
print(sum1)
for k in b:
    print(k,end=" ")