a=int(input())
b=int(input())
sum1=a+b
a1=0
b1=0
sum2=0
d=0
e=0
f=0
i=0
j=0
z=0
while(a>0):
    d=a%10                       
    if d!=0:
        a1=a1+d*(10**i)
        i=i+1
    a=a//10

while(b>0):
    e=b%10                       
    if e!=0:
        b1=b1+e*(10**j)
        j=j+1
    b=b//10

while(sum1>0):
    f=sum1%10                       
    if f!=0:
        sum2=sum2+f*(10**z)
        z=z+1
    sum1=sum1//10

if a1+b1==sum2:
    print("YES")  
else:
    print("NO")


