n=int(input())
n1=0
n2=0
sum1=0
sum2=0
if n%2==0:
    n1=n//2
    sum1=n1*(n1+1)
    sum2=n1*n1
    print(sum1-sum2)
else:
    n1=(n+1)//2
    n2=n1-1
    sum1=n2*(n2+1)
    sum2=n1*n1
    print(sum1-sum2)
    