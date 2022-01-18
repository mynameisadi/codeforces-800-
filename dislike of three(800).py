t=int(input())
while(t>0):
    n=int(input()) 
    sum1=0 
    for i in range(1,2000):
        if i%3!=0 and i%10!=3:
            sum1=sum1+1
            if sum1==n:
                print(i)
            

    t=t-1
