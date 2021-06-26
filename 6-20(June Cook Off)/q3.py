def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
for _ in range(II()):
    n = II()
    a = L()
    seven=[1,2,3,4,5,6,7]
    c=0
    for i in a:
        if (len(seven)==0):
            break
        if (i in seven):
            seven.remove(i)
        c+=1

    print(c)