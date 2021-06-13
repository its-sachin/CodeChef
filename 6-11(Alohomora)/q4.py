import math

def part(M, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i][0] < pivot[0] or (M[i][0] == pivot[0] and M[i][1] < pivot[1])):
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

for _ in range(int(input())):
    n = int(input())
    a = []
    s = []


    for i in range(n):
        x,y,v = map(int,input().split())
        s.append((x,y,v))
        a.append((x,y,v))

    sortC(s,0,n-1)

    for 
    # print(s)


