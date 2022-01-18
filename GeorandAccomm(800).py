n=int(input())
sum1=0
while(n>0):
    m,o=[int(x) for x in input().split()]
    if o-m>=2:
        sum1+=1
    n-=1
print(sum1)
