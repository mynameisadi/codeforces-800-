n=int(input())
arr=[int(i) for i in input().split()]
mini=101
maxi=0
sum1=0
o=0
p=0
for j in range(n):
    if arr[j]>maxi:
        maxi=arr[j]
        p=j

for k in range(n):
    if arr[k]<=mini:
        mini=arr[k]
        o=k

for x in range(p,0,-1):
    arr[x],arr[x-1]=arr[x-1],arr[x]
    sum1=sum1+1
for z in range(o,n-1,1):
    arr[z],arr[z+1]=arr[z+1],arr[z]
    sum1=sum1+1
if p>o:
    print(sum1-1)
else:
    print(sum1)
  
    


