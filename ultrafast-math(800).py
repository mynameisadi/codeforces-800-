n=input()
n1=input()
n2=""
for i in range(len(n)):
    if n[i]==n1[i]:
        n2=n2+"0"
    else:
        n2=n2+"1"
print(n2)