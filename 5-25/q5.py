
def lcm(a,b):
    if (a>b):
        c=a
        d=b
    else:
        c=b
        d=a
    r = c%d
    while(r!=0):
        c = d
        d = r
        r = c%d

    g = d
    l = int(int(a*b))/int(g)
    return l

def func(array,k):
    if (len(array)==0):
        return 0
    l = array[0]
    i = 1
    while(i<len(array)):
        l = lcm(l,array[i])
        i+=1

    ans= int(k/l)
    return ans




num = int(input())
for i in range(num):
    n,k = (input()).split(" ")
    n = int(n)
    k = int(k)
    array = input().split(" ")

    for j in range(n):
        array[j] = int(array[j])

    print(func(array,k))