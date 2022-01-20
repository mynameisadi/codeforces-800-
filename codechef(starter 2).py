t=int(input())
while(t>0):
    k=int(input())
    sum1=0
    for i in range(1,k):
        sum1=2**i
        if sum1==k:
            print(i)
            break
    t=t-1