t=int(input())
while(t>0):
    a,b,c=[int(x) for x in input().split()]  
    if a>50:
        print("A")
    elif b>50:
        print("B")
    elif c>50:
        print("C")
    else:
        print("NOTA")
    t=t-1