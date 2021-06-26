def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())

def get(a,z):


for _ in range(II()):
    n = II()
    a=L()
    dup = {}
    same = []
    p = (-1,-1)
    z=0
    for i in range(n):
        if (a[i]==0):
            z+=1
            if (z==1):
                same = [i,i]
        else:
            if(i%2!=same[0])
        if (len(same) == 0):
            if (dup.get(a[i]) != None):
                same = [dup.get(a[i]),i]
            else:
                dup[a[i]] = i
    if (z==n or len(same) == 0):
        print(-1)
    else:
        even =a[0]
        odd = 0
        for i in range(n):
            


