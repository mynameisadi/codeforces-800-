n=input()
a=dict()
sum1=0
for i in n:
    a[i]=a.get(i,0)+1
sum1=len(a)
if sum1%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
