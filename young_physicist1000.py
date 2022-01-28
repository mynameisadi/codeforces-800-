t=int(input()) 
sum1=0
sum2=0
sum3=0
while(t>0):
    arr=[int(x) for x in input().split()]
    sum1+=arr[0]
    sum2+=arr[1] 
    sum3+=arr[2]
    t=t-1
if sum1==0 and sum2==0 and sum3==0:
    print("YES")
else:
    print("NO")