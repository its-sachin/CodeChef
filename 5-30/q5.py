def func(queue,n):
    i = 0
    j = len(queue) - 1
    ans = 0

    pop = []
    for k in range(n):
        pop.append(k+1)

    while (len(pop) != 0):
        done = False
        if (queue[i] in pop):
            pop.remove(queue[i])
            i += 1
            ans += 1
            done = True
        if (queue[j] in pop):
            pop.remove(queue[j])
            j -= 1
            ans += 1
            done = True
        if (done == False):
            k = 1
            found = False
            temp = 0
            while(found == False):
                if (queue[i+k] in pop):
                    found = True
                    temp = 1
                    pop.remove(queue[i+k])
                    k += 1
                elif (queue[j-k] in pop):
                    found = True
                    temp = 2
                    pop.remove(queue[j-k])
                    k += 1
                else:
                    k+=1

            if (temp == 1):
                i += k
                ans += k
            else:
                i -=k
                ans += k
    return ans


num = int(input())

for i in range(num):

    n,m = (input()).split(" ")
    n,m = int(n),int(m)
    queue = input().split(" ")

    for j in range(m):
        queue[j] = int(queue[j])

    print(func(queue,n))