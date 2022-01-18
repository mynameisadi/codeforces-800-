k,r=[int(x) for x in input().split()]
i=1
j=1
s=0
while(True):
    s=k*i
    if s%10==0:
        print(i)
        break
    elif s%10==r:
        print(i)
        break
    i=i+1

