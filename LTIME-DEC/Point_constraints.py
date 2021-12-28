MOD = 998244353
for _ in range(int(input())):
    n,m,d = map(int,input().split())
    a = [d]*n
    for i in range(m):
        ci,bi = map(int,input().split())
        a[ci-1] = min(a[ci-1],d//bi)
    
    for i in range(n-2,-1,-1):
        a[i] = min(a[i],a[i+1])

    last = [1]*a[0]
    for i in range(1,n):
        for j in range(1,len(last)):
            last[j] = (last[j] + last[j-1])%MOD
        last.extend([last[-1]]*(a[i]-a[i-1]))
        print(last)
    ans = 0
    for i in last:
        ans = (ans+i)%MOD
    print(ans)