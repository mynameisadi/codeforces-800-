n=int(input())
s=input()
w=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        w+=1
print(w)