n=int(input())
a=0
sum1=0
while(n>0):
    a=n%10
    if a==4 or a==7:
        sum1+=1
    n=n//10
if sum1==4 or sum1==7:
    print("YES")
else:
    print("NO")
