for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b = [i for i in a]
    b.sort()

    i = 0; ans = 0
    while(i<n):
        while(i<n and a[i]==b[i]):i+=1
        if(i>=n):break
        mx = a[i]; mn = b[i]; c = 0
        while(i<n):
            if(mx==a[i]):
                c+=1
            elif(mx<a[i]):
                mx = a[i]; c=1
            if(mx==b[i]):
                c-=1
            i+=1
            if(c==0):
                ans += mx-mn
                break
    print(ans)