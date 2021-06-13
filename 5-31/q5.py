def gcd(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

def merge(group,same,n):

    i=0
    group[same[i]].append(n)
    while(i<len(same)-1):
        j=same[i+1]
        for k in group[j]:
            if (k not in group[same[i]]):
                group[same[i]].append(k)
        group.remove(group[j])
        i+=1

def func(n):

    group = []

    i = 2

    while(i<=n):
        done = False
        same = []
        for g in range(len(group)):
            for j in group[g]:
                if (gcd(j,i) != 1):
                    same.append(g)
                    done = True
                    break
            # print(g,group,same)

        if (done == False):
            group.append([i])
        else:
            if (len(same) > 1):
                merge(group,same,i)
        i+=1

    # print(group)
    return len(group)



num = int(input())

for i in range(num):
    n  = int(input())

    print(func(n))