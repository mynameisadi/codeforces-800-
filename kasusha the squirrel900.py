n,k=[int(x) for x in input().split()]
s=input()
sum1=0
b=0
flag=True
if s[len(s)-1]=="#":
    print("NO")
else:
    for i in range(1,len(s)):
        if s[i]=="." and i-b<=k:
            b=i
        elif s[i]=="." and i-b>k:
            flag=False
            break
    if (flag):
        print("YES")
    else:
        print("NO")



    