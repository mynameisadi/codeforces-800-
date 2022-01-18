arr=[int(x) for x in input().split()]
arr.sort()
for i in range(3):
    print(arr[3]-arr[i],end=" ")