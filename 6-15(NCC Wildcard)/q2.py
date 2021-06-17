for _ in range(int(input())):
    n = int(input())
    array = map(int,input().split())

    even = 0
    for i in array:
        if (i%2==0):
            even+=1

    print((3**n)-(2**even))

    