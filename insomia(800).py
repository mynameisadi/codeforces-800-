n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
a=set()
i=1
while(n1*i<=n5):
    a.add(n1*i)
    i+=1
j=1
while(n2*j<=n5):
    a.add(n2*j)
    j+=1
z=1
while(n3*z<=n5):
    a.add(n3*z)
    z+=1
k=1
while(n4*k<=n5):
    a.add(n4*k)
    k+=1
if len(a)==n5:
    print(n5)
else:
    print(len(a))
