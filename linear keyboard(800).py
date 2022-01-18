t=int(input())
while(t>0):
    a=input()
    b=input()
    sum1=0
    for i in range(1,len(b)):
        sum1+= abs(a.index(b[i])-a.index(b[i-1]))
    print(sum1)
    t=t-1