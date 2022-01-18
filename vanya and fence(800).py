n,m=[int(x) for x in input().split()]
a=[int(i) for i in input().split()]
sum1=0
for j in a:
    if j > m:
        sum1+=2
    else:
        sum1+=1
print(sum1)