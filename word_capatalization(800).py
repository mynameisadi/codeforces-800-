n=input()
s=""
if ord(n[0])>=65 and ord(n[0])<=90:
    print(n)
else:
    s=s+chr(ord(n[0])-32)
    for i in range(1,len(n)):
        s=s+n[i]
    print(s)