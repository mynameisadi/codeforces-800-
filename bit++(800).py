n=int(input())
x=0
while(n>0):
    s=input()
    if s=="++X" or s=="X++":
        x+=1
    if s=="--X" or s=="X--":
        x-=1
    n=n-1
print(x)