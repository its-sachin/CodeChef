def func(n,x,y,z):
    c10 = x/10
    c5 = y/5
    c1 = z

    cm = min(c10,c5,c1)

    if (cm==c10):
        a = n//10
        n = n%10

        cm = min(c5,c1)

        if (cm==c5):
            b = n//5
            c = n%5
        else:
            b = 0
            c = n
    
    elif (cm==c5):
        a=0
        b=n//5
        c=n%5

    else:
        a=0
        b=0
        c=n

    # print(a,b,c)
    return (a*x)+(b*y)+(c*z)


    

for _ in range(int(input())):
    n,x,y,z = input().split(" ")
    n,x,y,z = int(n),int(x),int(y),int(z)

    print(func(n,x,y,z))
