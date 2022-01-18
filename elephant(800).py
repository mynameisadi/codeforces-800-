n=int(input())
sum1=0
while(n>0):
    if n>=5:
        n-=5
        sum1+=1
    if n>=4 and n<5:
        n-=4
        sum1+=1
    if n>=3 and n<4:
        n-=3
        sum1+=1
    if n>=2 and n<3:
        n-=2
        sum1+=1
    if n>=1 and n<2:
        n-=1
        sum1+=1
print(sum1)
