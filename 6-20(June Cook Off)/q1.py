def I():
    return input()
def II():
    return int(I())
def M():
    return map(int,I().split())
def L():
    return list(M())
# for _ in range(II())

def search(a, n, val):

    i = 0
    j = n 
    mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (a[mid]== val):
            return mid
 
        if (val < a[mid]) :

            if (mid > 0 and val > a[mid - 1]):

                if (val - a[mid - 1] >= a[mid] - val):
                    return mid
                else:
                    return mid - 1
 
            j = mid
         
        else :

            if (mid < n - 1 and val < a[mid + 1]):

                if (val - a[mid] >= a[mid+1] - val):
                    return mid+1
                else:
                    return mid
                 
            i = mid + 1
         
    return mid

def notC(c):
    if(c==1):
        return -1
    else:
        return 1

def get(n,a,k):
    if (n%2==0):
        c=1
    else:
        c=-1

    if (k<a[0]):
        return c
    elif(k>a[n-1]):
        return 1
    elif (k==a[0] or k==a[n-1]):
        return 0

    else:
        l = search(a,n,k)
        if (a[l]==k):
            return 0
        if (l==0):
            return notC(c)
        if (a[l]<k):
            l-=1

        if (l%2==0):
            return c
        else:
            return notC(c)
        
        return c
                

n,q = M()
a=L()
a.sort()
for _ in range(q):
    k = II()
    c=get(n,a,k)
    if (c==1):
        print("POSITIVE")
    elif(c==-1):
        print("NEGATIVE")
    else:
        print(c)
