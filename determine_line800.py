from re import S


t=int(input())
s=t
d=dict()
while(t>0):
    arr=[int(x) for x in input().split()]
    for i in range(1,len(arr)):  
        d[arr[i]]=d.get(arr[i],0)+1
    
    t=t-1

for j in d.keys():
    if d[j]==s:
        print(j,end=" ")