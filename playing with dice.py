a,b=[int(x) for x in input().split()]
sum1=0
sum2=0
sum3=0
for i in range(1,7):
    if abs(i-a)<abs(i-b):
        sum1=sum1+1
    elif abs(i-a)>abs(i-b):
        sum2=sum2+1  
    elif abs(i-a)==abs(i-b):
        sum3=sum3+1
print(sum1,sum3,sum2)
