for _ in range(int(input())):
    x1,x2,x3,r = input().split(" ")
    x1,x2,x3,r = int(x1),int(x2),int(x3),int(r)

    if(x1<x2):
        temp =x1
        x1=x2
        x2=temp

    if (x3>=x1):
        if (x3-x1>r):
            ans = (x1-x2)
        else:
            ans = (x1-x2-(r-(x3-x1)))
    elif (x3<=x2):
        if (x2-x3>r):
            ans = (x1-x2)
        else:
            ans = (x1-x2-(r-(x2-x3)))
    else:
        if (x3-x2>r):
            if (x1-x3>r):
                ans = (x1-x2-2*r)
            else:
                ans = (x3-x2-r)
        else:
            if (x1-x3>r):
                ans = (x1-x3-r)
            else:
                ans = 0

    if (ans <0):
        ans = 0
    print(ans)

