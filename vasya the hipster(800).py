n,m=[int(x) for x in input().split()]
if n==m:
    print(n,end=" ")
    print("0")
if n>m:
    print(m,end=" ")
    print((n-m)//2)
if m>n:
    print(n,end=" ")
    print((m-n)//2)
    