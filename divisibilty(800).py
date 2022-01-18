import math
n=int(input())
while(n>0): 
    a,b=[int(x) for x in input().split()]
    c=0
    if a%b==0 or a==b:
        print("0")
    else:
        if a<b:
            print(b-a)
        else:
            c=a/b
            c=math.ceil(c)*b
            print(c-a) 
       
    n=n-1

'''n=int(input())
while(n>0): 
    a,b=[int(x) for x in input().split()]
    i=0
    if a%b==0:
        print("0")
    else:
        c=0
        while(True):
            i=i+1
            c=b*i
            if c>a :
                print(c-a)  
                break
            
    n=n-1'''