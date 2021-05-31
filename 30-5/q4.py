# def part(M, left, right):

#     out = left-1
#     pivot = M[right]
    
#     i = left
#     while(i < right):
#         if (M[i][0] < pivot[0] or (M[i][0] == pivot[0] and M[i][1] > pivot[1])):
#             out+= 1

#             temp = M[out]
#             M[out] = M[i]
#             M[i] = temp
#         i +=1
    
#     out += 1
#     temp = M[right]
#     M[right] = M[out]
#     M[out] = temp

#     return out

# def sortC(M, low, high):

#     if(low<high):
        
#         pivot = part(M,low,high)

#         sortC(M,low,pivot-1)
#         sortC(M,pivot+1,high)
            



def func(k,f,se):
    # print(se)
    time = 0
    prevE = 0
    # prevS = 0

    for i in se:
        currS = i[0]
        currE = i[1]

        # if (currS == prevS):

        if (currS > prevE):
            time += (currS - prevE)
        prevE = max(currE,prevE)
        # prevS = currS

    if (prevE < f):
        time += (f-prevE)

    print(time)
    if (time >= k):
        return "YES"
    return "NO"


num = int(input())

for i in range(num):

    n,k,f = (input()).split(" ")
    n,k,f = int(n),int(k),int(f)

    se = []
    for j in range(n):
        s,e = input().split(" ")
        s,e = int(s),int(e)
        se.append((s,e))

    # sortC(se,0,n-1)
    print(func(k,f,se))