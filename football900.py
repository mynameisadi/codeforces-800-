n=input()
sum1=0
sum2=0
flag=True
for i in n:
    if i=="0":
        sum1+=1
        sum2=0
    else:
        sum2+=1
        sum1=0
    if (sum1>=7 and sum2==0) or (sum2>=7 and sum1==0):
        flag=False
        print("YES")
        break 
    elif (sum1>=7 and sum2>0) or (sum2>=7 and sum1>0):
        sum1=0
        sum2=0
if flag==True:
    print("NO")   