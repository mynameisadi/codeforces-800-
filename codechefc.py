t=int(input()) 
while(t>0):
    n1=int(input())
    a=[]
    b=[]
    s=n1
    sum1=0
    sum2=0
    while(s>0):
        n,m=[int(x) for x in input().split()]
        a.append(n)
        b.append(m)
        s=s-1
    a.sort()
    b.sort()
    i=0
    j=0
    for i in range(n1):
        while(i<n1-1 and a[i]==a[i+1]):
            i=i+1
        sum1=sum1+1

    for j in range(n1):
        while(j<n1-1 and b[j]==b[j+1]):
            j=j+1
        sum2=sum2+1
    print(sum1+sum2)
    t=t-1