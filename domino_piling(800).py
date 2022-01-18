m,n=[int(x) for x in input().split()]
a=0
s=m*n
if s<=1:
    print(a)
else:
    if s%2==0:
        print(s//2)
    else:
        for i in range(1,s):
            a=2*i
            if a>s:
                a=a-2
                print(a//2)
                break
