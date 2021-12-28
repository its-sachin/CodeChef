for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    s = list(s)
    ans = []; ans[:] = s[:]
    i = k-1; got =False
    for j in range(k):
        ans[i] = s[j]
        if(got):
            i+=2
        else:
            i-=2
            if(i==-2):
                i=1
                got=True
            elif(i==-1):
                i=0
                got=True
    
    print(''.join(ans)) 