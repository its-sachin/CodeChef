import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n = II()
    a = L()
    e = []
    o = []
    for i in a:
        if(i%2==0):
            e.append(i)
        else:
            o.append(i)
    for i in e:
        print(i,end=" ")
    for i in o:
        print(i,end=" ")
    print("")