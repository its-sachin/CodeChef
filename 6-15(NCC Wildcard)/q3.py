def func(p,n):
    if (n==2):
        min=p[0]
        d = min
        for i in range(1,3):  
            d+=p[i]  
            if (p[i]<min):
                min = p[i]
        d-=min

        max = p[3]
        d-=max
        for i in range(3,6):  
            d+=p[i]  
            if (p[i]>max):
                max = p[i]
        d+=max
        return d,min

    else:
        v1 = p[0]
        p.remove(v1)
        v2 = p[1]
        p.remove(v2)
        v3 = p[2]
        p.remove(v3)

        d,m = func(p,n-1)

        if (v1+v2>m+v3):
            return (d-m+v1+v2-v3)


        

n = int(input())
p = map(int,input().spit())
