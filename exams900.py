import math
n,k=[int(x) for x in input().split()]
c=n*2
d=0

if c==k:
    print(n)
else:
    d=k-c
    if d<=0 or d>=n :
        print("0")
    else:
        print(n-d)
