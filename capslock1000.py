s=input()
flag1=True
s1=""
if ord(s[0])>=65 and ord(s[0])<=90:
    for x in s:
        if ord(x)>=97 and ord(x)<=122:
            flag1=False
            break
    if (flag1):
        for i in range(len(s)):
            if ord(s[i])>=97 and ord(s[i])<=122:
                s1=s1+chr(ord(s[i])-32)
            else:
                s1=s1+chr(ord(s[i])+32)
        print(s1)
    else:
        print(s)


elif ord(s[0])>=97 and ord(s[0])<=122:
    for y in range(1,len(s)):
        if ord(s[y])>=97 and ord(s[y])<=122:
            flag1=False
            break

    if (flag1):
        for j in range(len(s)):
            if ord(s[j])>=65 and ord(s[j])<=90:
                s1=s1+chr(ord(s[j])+32)
            else:
                s1=s1+chr(ord(s[j])-32)
        print(s1)
    else:
        print(s)


