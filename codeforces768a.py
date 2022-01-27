t=int(input())
while(t>0):
    n=int(input())
    arr1=[int(x) for x in input().split()]
    arr2=[int(y) for y in input().split()]
    a=0
    b=0
    for i in range(n):
        if arr1[i]>arr2[i]:
            arr1[i],arr2[i]=arr2[i],arr1[i]
    a=max(arr1)
    b=max(arr2)
    print(a*b)
    
    t=t-1