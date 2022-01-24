n=int(input())
s=input()
s=s.split(" ")
sum3=[]

for i in s:
    sum2=0
    for j in i:
        if ord(j)>=65 and ord(j)<=90:
            sum2+=1
    sum3.append(sum2)

print(max(sum3))

