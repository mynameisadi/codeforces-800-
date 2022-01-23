t=int(input())
while(t>0):
    x,y,z=[int(i) for i in input().split()]
    if y<=x and z>=x:
        print("PIZZA")
    elif y<=x and z<=x:
        print("PIZZA")
    elif y>x and z<=x:
        print("BURGER")
    else:
        print("NOTHING")
    t=t-1