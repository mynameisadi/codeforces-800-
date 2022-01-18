s=input()
t=input()
s1=""
for i in range(len(s)-1,-1,-1):
    s1=s1+s[i]
if s1==t:
    print("YES")
else:
    print("NO")