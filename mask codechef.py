t=int(input())
while(t>0):
    sum1=0
    n,m=[int(x) for x in input().split()]
    sum1=n-m
    print(min(sum1,m))
    t=t-1