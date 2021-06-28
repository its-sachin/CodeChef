import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    a = I()
    if(a[0]!="1"):
        a = "1"+a
    else:
        a = a[0]+"0"+a[1:]
    print(a)