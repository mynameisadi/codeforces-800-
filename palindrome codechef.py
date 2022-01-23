n=int(input())
while(n>0):
    s=""
    m=int(input())  
    for i in range(m):
        if i%3==0:
            s=s+"a"
        elif i%3==1:
            s=s+"b"  
        elif i%3==2:
            s=s+"c"
    print(s)
    n=n-1