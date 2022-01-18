n=int(input())
arr=[1,5,10,20,100]
a=n
i=-1
sum1=0
while(a>0):
    if a>=arr[i]:
        sum1=sum1+(a//arr[i])
        a=a%arr[i]
        i=i-1
    else:
        i=i-1
print(sum1)


