n=int(input())
while(n>0):
    m=int(input())
    if m%2==1:
        print((m-1)//2)
    if m%2==0:
        print((m-2)//2)
    n=n-1
