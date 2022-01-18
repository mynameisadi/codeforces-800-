n=int(input())
arr=[int(x) for x in input().split()]
flag=True
for i in arr:
    if i==1:
        flag=False
        print("HARD")
        break
if flag==True:
    print("EASY")