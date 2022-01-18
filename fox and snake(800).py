n,m=[int(x) for x in input().split()]
n1=[1,5,9,13,17,21,25,29,33,37,41,45,49]
n2=[3,7,11,15,19,23,27,31,35,39,43,47]
for i in range(0,n):
    if i%2==0:
        for j in range(0,m):
            print("#",end="")
        if i<n-1:
            print()
    if i in n1:
        for p in range(0,m):
            if p!=m-1:
                print(".",end="")
            else:
                print("#",end="")
        if i<n-1:
            print()
    if i in n2:
        for p in range(0,m):
            if p!=0:
                print(".",end="")
            else:
                print("#",end="")
        if i<n-1:
            print()
    
