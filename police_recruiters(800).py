n=input()
arr=[int(x) for x in input().split()]
sum1=0
police=0
for i in arr:
    if i<0 and police==0:
        sum1=sum1+1
    elif i>0:
        police=police+i
    elif i<0 and police>0:
        police=police-1
print(sum1)


