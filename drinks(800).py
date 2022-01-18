n=int(input())
arr=[int(x) for x in input().split()]
sum1=0
for i in arr:
    a=0
    if i!=0:
        a=100/i
        sum1=sum1+a**(-1)
print((sum1/n)*100)
