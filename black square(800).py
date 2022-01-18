a=[int(x) for x in input().split()]
s=input()
sum1=0
for i in s:
    sum1=sum1+a[int(i)-1]
print(sum1)