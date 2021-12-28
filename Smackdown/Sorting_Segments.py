for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    b = []
    for i in range(1,n+1):
        b.append(a[i-1]-i)
    print(b)