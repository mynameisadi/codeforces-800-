n,k=[int(x) for x in input().split()]
s=240-k 
sum1=0
flag=True
for i in range(1,n+1):
    sum1=sum1+5*i
    if sum1>s:
        flag=False
        print(i-1)
        break
if flag:
    print(n)

