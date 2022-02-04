n=int(input())
d={}
max1=0
while(n>0):
    a=input()
    d[a]=d.get(a,0)+1
    n=n-1
for x in d.values():
    if x>max1:
        max1=x 
for j in d.keys():
    if d[j]==max1:
        print(j)
