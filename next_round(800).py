n,k=[int(i) for i in input().split()]
arr=[int(x) for x in input().split()]
sum=0
for j in range(0,n):
    if arr[j]>0 and arr[j]>=arr[k-1]:
        sum+=1
print(sum)