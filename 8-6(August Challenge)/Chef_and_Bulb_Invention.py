for _ in range(int(input())):
    n,p,k = map(int,input().split())
    r=p%k
    num=n//k
    if(n%k>=r):
        num+=1
    print(r*num + p//k + 1)