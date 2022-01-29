n,m=[int(x) for x in input().split()]
arr=[int(y) for y in input().split()]
sum1=0
for k in arr:
    if k+m<=5:
        sum1+=1
if sum1>=3:
    print(sum1//3)
else:
    print("0")
