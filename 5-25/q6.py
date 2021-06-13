def func(n):
    c = False
    o =False
    d = False
    e = False
    E = False


    for i in range(len(n)):
        if (i != 0 and i != len(n)-1):
            if (n[i]=='e'):
                e = True
            if (n[i] == 'E'):
                E =True
        if (n[i] == 'C'):
            c = True
        if (n[i] == 'o'):
            o = True
        if (n[i] == 'D'):
            d = True

    if (c and o and d and e and E):
        return "SELECTED"
    return "REJECTED"

num = int(input())
for i in range(num):
    n = (input())
    print(func(n))