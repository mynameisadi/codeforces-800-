n,k,x=[int(x) for x in input().split()]
arr1=[int(y) for y in input().split()]  
sum1=0
for i in range(len(arr1)-k):
    sum1=sum1+arr1[i]
sum1=sum1+(k*x) 
print(sum1)