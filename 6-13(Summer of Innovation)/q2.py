mod = 1000000007
for _ in range(int(input())):
    a,Q = map(int,input().split())
    if (a!=1):
        mi = ((a-1)**2)%mod
    # qmax = -1
    # powers = []
    for i in range(Q):
        q = int(input())
        if (a==1):
            print(((((q%mod)*((q+1)%mod)//2)%mod + 1)%mod))
        else:
            an = pow(a,q,mod)
            a2 = pow(a,2,mod)
            a1 = a%mod
            n1 = (an*((a2-a1+1)%mod))%mod
            n2 = (((a1)*(q+1)%mod)%mod - (q%mod))%mod
            
            ans = ((n1-n2)/(mi))%mod


            print(int(ans))

