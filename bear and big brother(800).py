a,b=[int(x) for x in input().split()]
sum1=a
sum2=b
c=0
if a==b:
    print("1")
else:
    if a>b:
        c=a
    else:
        c=b
    for i in range(1,10):
        sum1=sum1*3
        sum2=sum2*2
        if sum1>sum2:
            print(i)
            break