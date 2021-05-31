def func(x,m,d):
    return min(x*m,x+d)

num = int(input())

for i in range(num):

    x,m,d = (input()).split(" ")
    x = int(x)
    m = int(m)
    d = int(d)

    print(func(x,m,d))