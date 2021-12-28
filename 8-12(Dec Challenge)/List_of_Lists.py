for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    mx = max(d.values())
    if(mx == n):
        print(0)
    elif(mx == 1):
        print(-1)
    else:
        print(n-mx+1)