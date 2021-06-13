for _ in range(int(input())):
    n = int(input())
    m = int(input())

    array=map(int,input().split())

    nc = 0
    for i in array:
        if ((i%5 != 0) or (i<5*m) or (i>55*m)):
            nc+=1

    print(n-nc)