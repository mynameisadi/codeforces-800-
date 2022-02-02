n=int(input())
arr=[int(x) for x in input().split()]  
sum1=0  
sum2=0  
sum3=0  
for i in range(0,n,3):
    sum1=sum1+arr[i]
for i in range(1,n,3):
    sum2=sum2+arr[i]
for i in range(2,n,3):
    sum3=sum3+arr[i]
a=max(sum1,sum2,sum3)
if a==sum1:
    print("chest")  
elif a==sum2:
    print("biceps")
elif a==sum3:
    print("back")