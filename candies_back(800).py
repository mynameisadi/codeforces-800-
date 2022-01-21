n,m=map(int,input().split())
sum2=0   
sum1=0
if n%m==0:
    sum1=n//m
    arr=[sum1]*m
    for i in range(m):
        print(arr[i],end=" ")

else:
    sum1=n//m
    sum2=n%m
    arr=[sum1]*m
    for j in range(m-1,m-sum2-1,-1):
        arr[j]=arr[j]+1
    for k in range(m):
        print(arr[k],end=" ")
