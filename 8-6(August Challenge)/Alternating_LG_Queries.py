import math
for _ in range(int(input())):
    n,q = map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(q):
        x,l,r=map(int,input().split())
        l-=1
        r-=1
        f=(r-l)%2
        if(x==2):
            f=1-f
        ans=a[r]
        for j in range(r-1,l-1,-1):
            if(f==1):
                ans=math.gcd(ans,a[j])
            else:
                ans=(ans*a[j])//math.gcd(ans,a[j])
            f=1-f

        print(ans)