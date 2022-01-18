n=int(input())
arr1=[int(i) for i in input().split()]
arr2=[int(j) for j in input().split()]
arr3=[]
for k in range(1,arr1[0]+1):
    if arr1[k] not in arr3:
        arr3.append(arr1[k])
for l in range(1,arr2[0]+1):
    if arr2[l] not in arr3:
        arr3.append(arr2[l])
flag=True
for y in range(1,n+1):
    if y not in arr3:
        flag=False
        print("Oh, my keyboard!")
        break
if flag==True:
    print("I become the guy.")
