k,n,w=[int(x) for x in input().split()]
sum1=0
for i in range(1,w+1):
    sum1=sum1+i*k

if sum1>=n:
    print(sum1-n)
else:
    print("0")