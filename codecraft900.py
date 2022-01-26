arr=["January","February","March","April","May","June","July","August","September","October","November","December"]
n=input()
m=int(input())
sum1=0
sum1=(arr.index(n)+1)+(m%12)
if sum1>12:
    sum1=sum1-12
    print(arr[sum1-1])
else:
    print(arr[sum1-1])
