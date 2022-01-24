t=int(input())
while(t>0):
    n,m=map(int,input().split())
    s=input()
    s3=list(s)
    s4=""
    
    for i in range(m):
        s1=[]
        for j in range(n):
            if s[j]=="0":
                if j==0 and s[j+1]=="1":
                    s1.append(j)
                elif (s[j-1]=="1") and (j==len(s)-1):
                    s1.append(j)
                elif j!=0 and j!=len(s)-1:
                    if (s[j-1]=="0" and s[j+1]=="1") or (s[j-1]=="1" and s[j+1]=="0"):
                        s1.append(j)
    
        for k in s1:
            s3[k]="1"
        s=""
        for o in s3:
            s=s+o
    for l in s3:
        s4=s4+l

    print(s4)

    t=t-1