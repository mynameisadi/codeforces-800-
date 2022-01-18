arr=[int(x) for x in input().split()]
a=set()
for i in arr:
    a.add(i)
if len(a)==4:
    print("0")
else:
    print(4-len(a))