x=input()
x1=set()
for i in x:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        x1.add(i)
print(len(x1))
