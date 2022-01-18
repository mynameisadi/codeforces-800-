arr=[int(x) for x in input().split()]
sum1=0
arr.sort()
sum1=(arr[2]-arr[1])+(arr[1]-arr[0])
print(sum1)