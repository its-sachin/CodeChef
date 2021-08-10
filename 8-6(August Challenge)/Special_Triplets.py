for _ in range(int(input())):
    n = int(input())
    ans=0
    for c in range(1,(n//2)+1):
        for i in range(2,(n//c)+1):
            curr = ((((n//c)-1)//i)+1)
            ans+=curr
    print(ans)