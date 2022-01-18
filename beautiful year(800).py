n=int(input())
for i in range(n+1,n+3000):
    d=dict()
    s=0
    x=i
    while(i>0):
        s=i%10
        d[s]=d.get(s,0)+1
        i=i//10
    flag=True
    for j in d.values():
        if j>1:
            flag=False
            break
    if flag==True:
        print(x)
        break

            


