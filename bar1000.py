alcohol=['ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WHISKEY', 'WINE']
n=int(input())
sum1=0
while(n>0):
    m=input()
    if (m.isnumeric()):
        if int(m)<18:
            sum1=sum1+1
    else:
        if m in alcohol:
            sum1=sum1+1
    n=n-1
print(sum1)
    