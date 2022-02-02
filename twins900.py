n=int(input())
arr=[int(x) for x in input().split()]
arr1=[]
l=n-1
while(l>=0):
    arr1.append(arr[l])
    l=l-1


sum1=0
sum2=0
k=0
for i in range(n):
    sum1=sum1+arr1[i]
    sum2=sum2+arr1[n-i-1]
    if sum2>=sum1:
        k=k+1
print(k)
    
    





