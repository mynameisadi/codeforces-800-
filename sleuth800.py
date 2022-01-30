n=input()
arr=n.split()
if arr[-1]=="?":
    s=arr[-2]
    if s[-1]=="a" or s[-1]=="A" or s[-1]=="e" or s[-1]=="E" or s[-1]=="i" or s[-1]=="I" or s[-1]=="o" or s[-1]=="O" or s[-1]=="u" or s[-1]=="U" or s[-1]=="Y" or s[-1]=="y":
        print("YES")
    else:
        print("NO")  
else:
    s=arr[-1] 
    if s[-2]=="a" or s[-2]=="A" or s[-2]=="e" or s[-2]=="E" or s[-2]=="i" or s[-2]=="I" or s[-2]=="o" or s[-2]=="O" or s[-2]=="u" or s[-2]=="U" or s[-2]=="y" or s[-2]=="Y":
        print("YES")
    else:
        print("NO")