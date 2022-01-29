t=int(input())
while(t>0):
    n,x,y=[int(x) for x in input().split()]
    a=[int(y) for y in input().split()]
    b=[int(z) for z in input().split()]
    c=[]
    for i in range(n):
        c.append(b[i]-a[i])
    flag=True
    for j in c:
        if j!=x and j!=y:
            flag=False
            break
    if (flag):
        print("YES")
    else:
        print("NO")
        
    t=t-1