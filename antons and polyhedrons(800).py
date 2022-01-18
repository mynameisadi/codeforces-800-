n=int(input())
Octahedron=8
Dodecahedron=12
Icosahedron=20
sum1=0
while(n>0):
    n1=input()
    if n1=="Tetrahedron":
        sum1=sum1+4
    elif n1=="Cube":
        sum1=sum1+6
    elif n1=="Octahedron":
        sum1=sum1+8
    elif n1=="Dodecahedron":
        sum1=sum1+12
    elif n1=="Icosahedron":
        sum1=sum1+20
    n=n-1
print(sum1)