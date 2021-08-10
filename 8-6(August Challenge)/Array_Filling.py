import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(m):
        x,y = map(int,input().split())
        a.append((x,y))
    a.sort(reverse=True)
    ans=0
    t=1
    d=0
    for i in range(m):
        t=(t*a[i][1])//math.gcd(t,a[i][1])
        k=(n//t)
        d2=n-k
        d1=d2-d
        d=d2
        ans+=a[i][0]*d1
        if(d==n):
            break
            
    print(ans)