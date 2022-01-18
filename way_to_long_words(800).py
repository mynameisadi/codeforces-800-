n=int(input())
while(n>0):
    a=0
    s=input()
    if len(s)>10:
        a=len(s)
        s=s[0]+ str(a-2) + s[a-1]
        print(s)    
    else:
        print(s)
    n=n-1