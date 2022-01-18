n=int(input())
mish=0
chris=0
while(n>0):
    a,b=[int(x) for x in input().split()]
    if a>b:
        mish=mish+1
    elif b>a:
        chris=chris+1
    n=n-1
if mish>chris:
    print("Mishka")
elif chris>mish:
    print("Chris")
else:
    print("Friendship is magic!^^")