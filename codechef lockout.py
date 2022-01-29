t=int(input())
while(t>0):
    arr=[int(x) for x in input().split()]
    if arr[0]+arr[1]==arr[2] or arr[1]+arr[2]==arr[0] or arr[0]+arr[2]==arr[1]:
        print("YES")  
    else:
        print("NO")
    t=t-1
        