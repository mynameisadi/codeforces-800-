rank=["6","7","8","9","T","J","Q","K","A"]
c=0
d=0
trump=input()
card1,card2=[str(x) for x in input().split()]
if trump==card1[1] and trump!=card2[1]:
    print("YES")
elif trump==card2[1] and trump!=card1[1]:
    print("NO")
elif trump!=card1[1] and trump!=card2[1] and card1[1]!=card2[1]:
    print("NO")
else:
    c=rank.index(card1[0])
    d=rank.index(card2[0])
    if c>d:
        print("YES")
    else:
        print("NO")

