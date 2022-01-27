n=int(input())
arr=[int(x) for x in input().split()]
sum1=0
sum2=0
sum3=0
for i in arr:
    if i==1:
        sum1=sum1+1
    elif i==2:
        sum2=sum2+1 
    elif i==3:
        sum3=sum3+1
    
sum4=0
if sum1==sum2 and sum1==sum3:
    sum4=sum1+sum2
    print(sum4)
else:
    if sum1>=sum2 and sum1>=sum3:
        sum4=sum2+sum3
        print(sum4)
    elif sum2>=sum3 and sum2>=sum1:
        sum4=sum1+sum3
        print(sum4)
    else:
        sum4=sum1+sum2
        print(sum4)
