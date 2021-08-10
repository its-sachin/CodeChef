for _ in range(int(input())):
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if(d.get(i)==None):
            d[i]=1
        else:
            d[i]+=1

    m=0
    for i in d:
        m=max(d[i],m)

    if(m==4):
        print(0)
    elif(m==3):
        print(1)
    else:
        print(2)
