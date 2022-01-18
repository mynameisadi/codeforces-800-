n=int(input())
while(n>0):
    n1=int(input())
    arr=[int(x) for x in input().split()]
    arr.sort()
    if n1==1:
        print("YES")
    else:
        i=0
        while(i<n1-1):
            flag=True
            if abs(arr[i]-arr[i+1])<=1:
                flag=False
                arr.pop(i)
                n1-=1
        
            if flag==True:
                i=i+1
            else:
                i=0
        if len(arr)==1:
            print("YES")
        else:
            print("NO")
        

    n=n-1