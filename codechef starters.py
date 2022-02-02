t=int(input())
while(t>0):
    arr=[]
    a,b=[int(x) for x in input().split()]
    for i in range(a-b):
        arr.append(1)
    flag=True
    for j in range(b):
        if a-b==0:
            flag=False
        else:
            arr.append(1)
            arr.append(1)
    if (flag):
        print(len(arr))
    else:
        print((2*a)-1)
    t=t-1