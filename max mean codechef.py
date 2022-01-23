n=int(input())
while(n>0):
    m=int(input())  
    arr=[int(x) for x in input().split()]
    sum1=0
    for j in arr:
        sum1=sum1+j
    sum2=0
    d1=0
    d2=0
    max1=0
    for k in range(m-1):
        sum2=sum2+arr[k]
        sum1=sum1-arr[k]
        d1=sum1/(m-k-1)
        d2=sum2/(k+1)
        if d1+d2>max1:
            max1=d1+d2
    print('%.6f'%max1)

    n=n-1
