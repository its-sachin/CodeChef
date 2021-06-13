import math

for _ in range(int(input())):
    xa,xb,Xa,Xb = map(int,input().split(" "))

    print(math.ceil(Xa/xa)+math.ceil(Xb/xb))