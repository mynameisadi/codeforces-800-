t=int(input())

while(t>0):
    x,y=[int(x) for x in input().split()]
    print(min(x//2,y//1))
    t=t-1