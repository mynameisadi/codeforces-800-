n=int(input())  
sum1=0  
i=1
sum2=0
while(True):
    sum1=(i*(i+1))//2
    sum2=sum2+sum1
    if sum2>n:
        print(i-1)
        break
    i=i+1
    