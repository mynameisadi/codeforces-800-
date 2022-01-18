n=int(input())
w=0
while(n>0):
    sum=0
    x,y,z=input().split()
    sum=int(x)+int(y)+int(z)
    if sum>=2:
        w+=1
    n=n-1
print(w)