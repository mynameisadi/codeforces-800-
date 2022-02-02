n=int(input())
while(n>0):
    a,b,c,p,q,r=[int(x) for x in input().split()]
    
    sum2=(p+q+r)/2

    if c+b+p>sum2 or a+c+q>sum2 or a+b+r>sum2 :
        print("YES")
    else:
        print("NO")

    n=n-1
