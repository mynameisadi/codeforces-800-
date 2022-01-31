s=input()  
arr=["a","e","i","o","u","A","E","I","O","U","Y","y"]
s1=""
for i in s:
    if i not in arr:
        if ord(i)>=65 and ord(i)<=90:
            s1=s1+"."
            s1=s1+chr(ord(i)+32)
        else:
            s1=s1+"."
            s1=s1+i
print(s1)
        
        