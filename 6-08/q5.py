x,y = input().split(" ")
x,y = int(x),int(y)

n,k = input().split(" ")
n,k = int(n),int(k)

dep= []

def dist(x1,y1):
    return ((x1-x)**2 + (y1-y)**2)**(0.5)

def part(M, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i][0] < pivot[0] or (M[i][0] == pivot[0] and M[i][1] == 'X')):
            out+= 1

            temp = M[out]
            M[out] = M[i]
            M[i] = temp
        i +=1
    
    out += 1
    temp = M[right]
    M[right] = M[out]
    M[out] = temp

    return out

def sortC(M, low, high):

    if(low<high):
        
        pivot = part(M,low,high)

        sortC(M,low,pivot-1)
        sortC(M,pivot+1,high)
            

for i in range(n):
    x1,y1,g = input().split(" ")
    dep.append((dist(int(x1),int(y1)),g))
    # print(x1,y1,dist(int(x1),int(y1)))

sortC(dep,0,n-1)
# print(dep)

scount = 0
nscount = 0

for i in range(k):
    # print(dep[])
    if (dep[i][1] == "S"):
        scount+=1
    else:
        nscount+=1

# print(nscount,scount)

if (scount>=nscount):
    print("IT IS EXHILARATING")
else:
    print("EASY AS CAKE")