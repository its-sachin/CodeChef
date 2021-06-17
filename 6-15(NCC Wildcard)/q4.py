import math

def nd(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
    
def pf(n):

    if (n==1):
        return 1

    c = 0
    i=0
    while n % 2 == 0:
        i+=1
        n = n / 2

    if (i>0):
        c+=1
        if (i!=1):
            c+=nd(i)
         
    for k in range(3,int(math.sqrt(n))+1,2):

        i=0
        while n % k== 0:
            i+=1
            n = n / k

        if (i>0):
            c+=nd(k)
            if (i!=1):
                c+=nd(i)
             
    if n > 2:
        c+=nd(n)

    return c
    
def sp(n):
    if (nd(n)==pf(n)):
        return True
    return False

# special = []
# for i range(1,2*(10**4)):
#     if(sp(i)):
#         special.append(i)

for _ in range(int(input())):

    a,b = map(int,input().split())
    c = 0
    i=0
    while(b>a):
        # print(b,a,i)
        if (sp(b-a-i)):
            c+=1
            a=b-i
            i=0
        else:
            i+=1

    print(c)