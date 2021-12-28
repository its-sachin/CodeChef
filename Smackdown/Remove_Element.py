for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if(len(a) > 1 and a[-1]+a[0]>k):
        print('NO')
    else:
        print('YES')
