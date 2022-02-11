t=int(input())
while(t>0):
    sum1=0
    a=0
    n,x=[int(i) for i in input().split()]
    a=n+1
    if x>n:
        while(x>=n+1):
            x=x-a
        print(x)
    else:
        print(x)
    t=t-1