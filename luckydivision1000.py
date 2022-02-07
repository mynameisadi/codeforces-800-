arr=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
n=int(input())
flag=True
for x in arr:
    if n%x==0:
        flag=False
        break
if (flag):
    print("NO")
else:
    print("YES")
