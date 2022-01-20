n,m=[int(x) for x in input().split()]
sum1=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
s=sum1.index(n)
if sum1[s+1]==m:
    print("YES")
else:
    print("NO")
