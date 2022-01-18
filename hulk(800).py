n=int(input())
s1="I hate"
s2="I love"
s3=""
for i in range(1,n+1):
    if i%2==1:
        s3=s3+s1
    else:
        s3=s3+s2
    if i!=n:
        s3=s3+" that "
print(s3+" it")
        
            