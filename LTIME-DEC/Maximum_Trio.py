for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx,m1,mn = -1,-1,a[0]
    for i in a:
        mn = min(mn,i)
        if(mx < i):
            m1 = mx
            mx = i
        elif(m1 < i):
            m1 = i
    print(max((m1-mn)*mx,(mx-mn)*m1))
        