n,m=[int(x) for x in input().split()]
m1 = []
for i in range(n):
   row = list(map(str,input().split()))
   m1.append(row)

sum1=0
for i in range(n):
    for j in range(m):
        if m1[i][j]=='W' or m1[i][j]=='B' or m1[i][j]=='G':
            sum1=sum1+1  
if sum1==(n*m):
    print("#Black&White")
else:
    print("#Color")
