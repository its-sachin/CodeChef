for _ in range(int(input())):
    n,p,k = map(int,input().split())
    n-=1
    t=(n%k)+1
    l=p%k
    d=(n//k)+1
    if(t>=l):
        a=l*d
    else:
        a=(t*d)+((d-1)*(l-t))
    print(a+(p//k)+1)
