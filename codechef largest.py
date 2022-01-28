t=int(input())

while(t>0):
    max1=0
    max2=0
    arr=[int(x) for x in input().split()]
    for x in arr:
        if x>max1:
            max1=x
    for j in arr:
        if j!=max1 and j>max2:
            max2=j  
    print(max2) 

    t=t-1