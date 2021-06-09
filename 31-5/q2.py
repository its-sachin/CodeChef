def func(t):
    if (t>=0 and t%2 == 0):
        return "YES"
    else:
        return "NO"


num = int(input())

for i in range(num):
    a,b,c,d,k = (input()).split(" ")
    a,b,c,d,k = int(a),int(b),int(c),int(d),int(k)

    t = k- abs(a-c) + abs(b-d)
    print(func(t))
    