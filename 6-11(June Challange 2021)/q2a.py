for _ in range(int(input())):
    D,d,P,Q = map(int,input().split(" "))

    rate = P
    i=0
    money = 0
    while(i<D):
        money += rate
        i+=1
        if (i%d==0):
            rate+=Q

    print(money)
        