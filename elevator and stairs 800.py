x , y, z, t1, t2, t3=map(int,input().split())
sum1=0
sum2=0

sum1=abs(x-y)*t1
if x!=z:
    sum2=(3*t3)+abs(x-z)*t2 +abs(x-y)*t2
else:
    sum2=(3*t3)+abs(x-y)*t2

if sum2<=sum1:
    print("YES")
else:
    print("NO")