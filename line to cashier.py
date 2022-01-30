n=int(input())
arr=[int(x) for x in input().split()]
arr2=[]
for i in range(n):
    sum1=0
    arr1=[int(y) for y in input().split()]
    for j in arr1:
        sum1=sum1+(j*5)
    arr2.append(sum1+arr[i]*15)

arr2.sort()
print(arr2[0])