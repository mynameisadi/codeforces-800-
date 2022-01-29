n=int(input())
arr=[int(x) for x in input().split()]  
a=0
arr1=[]
b=0
arr2=[]
for j in arr:
    if j%2==0:
        arr1.append(j)
        a+=1  
    elif j%2==1:
        arr2.append(j)
        b+=1
if a<b:
    for k in range(n):
        if arr[k]==arr1[0]:
            print(k+1)
else:
    for l in range(n):
        if arr[l]==arr2[0]:
            print(l+1)