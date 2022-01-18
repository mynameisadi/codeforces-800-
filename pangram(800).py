n=int(input())
m=input()
d=[0]*26
c=0
for i in m:
    c=ord(i)
    if c>=97 and c<=122:
        d[c-97]=d[c-97]+1
    else:
        d[c-65]=d[c-65]+1
flag=True
for j in d:
    if j==0:
        flag=False
        print("NO")
        break
if flag==True:
    print("YES")

