n=int(input())
n1=n
i=0
j=0
h=[]
a=[]
sum1=0
while(n>0):
    h1,a1=[int(x) for x in input().split()]
    h.append(h1)
    a.append(a1)
    n=n-1

while(i<n1):
    while(j<n1):
        if i!=j and (h[i]==a[j] or h[j]==a[i]):
            sum1=sum1+1
        j=j+1
    i=i+1
print(sum1)