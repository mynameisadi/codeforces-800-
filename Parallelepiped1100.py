import math
s1,s2,s3=[int(x) for x in input().split()]
a=math.sqrt((s1*s3)/s2)
b=math.sqrt((s1*s2)/s3)
c=math.sqrt((s2*s3)/s1)
d=4*(a+b+c)
print(int(d))
