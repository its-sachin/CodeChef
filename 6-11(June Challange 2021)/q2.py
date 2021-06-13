for _ in range(int(input())):
    D,d,P,Q = map(int,input().split(" "))

    k=D//d
    x=D - (k*d)

    print((k*P + ((k-1)*k*Q)//2)*d + x*(P+k*Q))
        

