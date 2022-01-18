n=input()
sum1=0
sum2=0
n1=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        sum1+=1
    else:
        sum2+=1
if sum1==sum2:
    for i in n:
        if ord(i)>=65 and ord(i)<=90:
            n1=n1+chr(ord(i)+32)
        else:
            n1=n1+i
elif sum1>sum2:
    for i in n:
        if ord(i)>=97 and ord(i)<=122:
            n1=n1+chr(ord(i)-32)
        else:
            n1=n1+i
elif sum2>sum1:
    for i in n:
        if ord(i)>=65 and ord(i)<=90:
            n1=n1+chr(ord(i)+32)
        else:
            n1=n1+i
print(n1)

        

    