j=int(input())
n=input()
sum1=0
sum2=0
for i in n:
    if i=="A" or i=="a":
        sum1+=1
    elif i=="D" or i=="d":
        sum2+=1
if sum1>sum2:
    print("Anton")
elif sum2>sum1:
    print("Danik")
else:
    print("Friendship")
