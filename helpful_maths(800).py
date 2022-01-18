arr=input().split("+")
arr.sort()
for i in range(0,len(arr)-1):
    print(arr[i]+"+",end="")
print(arr[len(arr)-1])