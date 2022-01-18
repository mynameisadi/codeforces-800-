n=int(input())
s=0
s1=0
while(n>0):
    a,b=[int(x) for x in input().split()]
    s=s-a
    s=s+b
    if s>=s1:
        s1=s
    n=n-1
print(s1)