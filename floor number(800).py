n=int(input())
while(n>0):
    c=0
    sum1=1
    a,b=[int(x) for x in input().split()]
    if a<=2:
        print("1")
    else:
        c=a-2
        if (c/b)==int(c/b):
            sum1=sum1+(c//b)
        else:
            sum1=sum1+(c//b)+1
        print(sum1)
    
    n=n-1
