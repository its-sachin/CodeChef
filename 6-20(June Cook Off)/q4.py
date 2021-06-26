def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())

for _ in range(II()):
    x1 , x2, y1, y2, z1, z2 = M()
    if (x2>=x1 and y2>=y1 and z2<=z1):
        print("yes")
    else:
        print("no")

