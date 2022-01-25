n=int(input())   
arr=[int(x) for x in input().split()]   
sum1=0
for i in arr:
    sum1+=i
    
sum2=0
sum3=0
if sum1%2==1:
    for j in arr:
        if j%2==1:
            sum2+=1
    print(sum2)
else:
    for k in arr:
        if k%2==0:
            sum3+=1
    print(sum3)

