n=int(input())   
arr=[int(x) for x in input().split()]
arr1=[]
arr2=[]
arr3=[]

if 1 in arr and 2 in arr and 3 in arr:
    for i in range(n):
        if arr[i]==1:
            arr1.append(i+1)
        elif arr[i]==2:
            arr2.append(i+1)  
        elif arr[i]==3:
            arr3.append(i+1)
    m=min(len(arr1),len(arr2),len(arr3))  
    print(m)
    for j in range(m):  
        arr4=[]
        arr4.append(arr1[j])
        arr4.append(arr2[j])
        arr4.append(arr3[j])
        for k in arr4:
            print(k,end=" ")
        print()
        
else:
    print("0")    