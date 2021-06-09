def part(M, left, right):

    out = left-1
    pivot = M[right]
    
    i = left
    while(i < right):
        if (M[i] > pivot):
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
            



def func(array,k,n):
    sortC(array,0,n-1)

    # print(array)
    a,x=0,0
    b,y=0,0


    for i in range(n):
        if (y>=k and x>=k):
            break
        elif (y==k-1 and x==k):
            b+=array[i]
            b+=array[i+1]
            y+=1
            i+=1
        else:
            if (i%2 == 0):
                a+=array[i]
                x+=1
            else:
                b+=array[i]
                y+=1

    return max(a,b)



num = int(input())

for i in range(num):
    n,k = (input()).split(" ")
    n,k = int(n),int(k)
    array = input().split(" ")

    for i in range(n):
        array[i] = int(array[i])

    print(func(array,k,n))