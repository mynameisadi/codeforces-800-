n=int(input())
a=0
if n==0:
    print("O-|-OOOO")
else:
    while(n>0):
        a=n%10
        if a<=4:
            s1="O-|"
            for i in range(a):
                s1=s1+"O"
            if len(s1)-1<=7:
                s1=s1+"-"
            if len(s1)-1<=7:
                for j in range(8-len(s1)):
                    s1=s1+"O"
            print(s1)
        else:
            s2="-O|"
            for k in range(a-5):
                s2=s2+"O"
            if len(s2)-1<=7:
                s2=s2+"-"
            if len(s2)-1<=7:
                for j in range(8-len(s2)):
                    s2=s2+"O"
            print(s2)

        n=n//10

