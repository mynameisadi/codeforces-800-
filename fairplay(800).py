t=int(input())
while(t>0):
    arr=[int(x) for x in input().split()] 
    a=max(arr[0],arr[1])
    b=max(arr[2],arr[3])
    c=0
    d=0
    for i in arr:
        if i>c:
            c=i
    for j in arr:
        if j>d and j!=c:
            d=j
    
    if (a==c or a==d) and (b==c or b==d):  
        print("YES")
    else:
        print("NO")
    
    t=t-1