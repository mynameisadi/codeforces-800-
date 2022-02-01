arr1=input()
arr2=input()
sum1=0
j=0
for i in range(len(arr2)):
    if arr2[i]==arr1[j] and j<len(arr1):
        sum1+=1
        j=j+1
print(sum1+1)