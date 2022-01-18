n=int(input())
while(n>0):
    d=dict()
    a=int(input())
    arr=[int(x) for x in input().split()]
    for i in arr:
        d[i]=d.get(i,0)+1
    for j in d.keys():
        if d[j]==1:
            print(arr.index(j)+1)
    n=n-1


    