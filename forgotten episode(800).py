n=int(input())  
arr=[int(x) for x in input().split()]
sum1=(n*(n+1)//2)
sum2=0
for i in arr:   
    sum2=sum2+i
print(sum1-sum2)