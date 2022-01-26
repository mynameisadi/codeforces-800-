s=input()
s1=0
sum1=0
sum2=0
for i in range(len(s)):  
    if ord(s[i])==94:
        s1=i

for j in range(0,s1+1):
    if ord(s[j])>=49 and ord(s[j])<=57:
        sum1=sum1+(int(s[j])*(s1-j))

for k in range(s1+1,len(s)):  
    if ord(s[k])>=49 and ord(s[k])<=57:
        sum2=sum2+(int(s[k])*(k-s1))

if sum1==sum2:
    print("balance")
else:
    if sum1>sum2:
        print("left")
    else:
        print("right")  