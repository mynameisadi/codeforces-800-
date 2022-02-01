n,k=[int(x) for x in input().split()]
arr=[int(y) for y in input().split()]
count=0
for i in arr:
    lucky=0
    s1=0
    while(i>0):
        s1=i%10
        if s1 == 4 or s1 == 7:
            lucky=lucky+ 1
        i=i//10
    
    if (lucky <= k):
        count += 1

print(count)

