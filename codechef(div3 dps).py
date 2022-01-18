n=int(input())
while(n>0):
    sum1=0
    sum2=0
    sum3=0
    a,b=[int(x) for x in input().split()]
    c,d=[int(y) for y in input().split()]
    e,f=[int(z) for z in input().split()]
    sum1=a+b
    sum2=c+d
    sum3=e+f
    
    sum1=max(sum1,sum2)
    sum3=max(sum1,sum3)
    print(sum3)
    n=n-1