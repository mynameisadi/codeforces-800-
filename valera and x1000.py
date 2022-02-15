n=int(input())
mat = [[str(j) for j in input()] for i in range(n)]
arr=[]
arr1=[]
for i in range(n):
    for j in range(n):
        if (i==j) or (i+j==n-1):
            arr.append(mat[i][j])
        else:
            arr1.append(mat[i][j])

flag=True
for k in range(len(arr)-1):
    if arr[k]!=arr[k+1]:
        flag=False
        break
flag1=True

if (flag):
    for l in arr1:
        if l in arr:
            flag1=False
            break

    if (flag1):
        flag2=True
        for q in range(len(arr1)-1):
            if arr1[q]!=arr1[q+1]:
                flag2=False
                break
        if (flag2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")