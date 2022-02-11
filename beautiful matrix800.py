mat = [[int(j) for j in input().split()] for i in range(5)]
sum1=0
a=0
b=0
flag=False
for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            flag=True
            a=i
            b=j
            break
    if (flag):
        break
sum1=abs(a-2)+abs(b-2)
print(sum1)