n=int(input())
arr=[int(i) for i in input().split()]
arr1=[0]*n
for j in range(0,n):
    arr1[arr[j]-1]=j+1
for k in arr1:
    print(k,end=" ")