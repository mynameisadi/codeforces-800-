a,b=[int(x) for x in input().split()]
sum1=0
sum2=0
while(a>0):
    a=a-1
    sum1+=1
    sum2=sum2+1
    if sum1==b:
        a=a+1
        sum1=0

print(sum2)