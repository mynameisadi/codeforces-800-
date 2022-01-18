n=int(input())
while(n>0):
    n1,n2=[int(x) for x in input().split()]  
    if n1==n2:
        print("0")
    else:
        if abs(n1-n2)%10==0:
            print(abs(n1-n2)//10)
        else:
            print((abs(n1-n2)//10)+1)
    n=n-1