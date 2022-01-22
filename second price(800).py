n=int(input())
arr=[int(x) for x in input().split()]
sum1=0
k=0
for j in range(n):
    if arr[j]>sum1:
        sum1=arr[j]
        k=j

sum2=0
for i in arr:
    if i>sum2 and i!=sum1:
        sum2=i
print(k+1,end=" ")
print(sum2)