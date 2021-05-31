def rem(array):
    i = 0
    copy = []
    while(i < len(array)):
        if (array[i]%3 != 0):
            array.remove(array[i])
        else:
            if (i !=0 and array[i] == array[i-1]):
                if (i != len(array)-1 and array[i]!=array[i+1]):
                    copy.append(array[i-1])
                    array.remove(array[i-1])
                    array.remove(array[i-1])
                    i-=1
                else:
                    array.remove(array[i-1])

            else:
                i+=1

    return copy

    # print(array)


def parray(array):
    for i in range(1,len(array)):
        k=array[i]
        j=i-1
        while(j>=0 and k<array[j]):
            array[j+1] = array[j]
            j-=1
        array[j+1] = k


def func(array1,array2):
    parray(array1)
    parray(array2)
    copy1 = rem(array1)
    copy2 = rem(array2)

    if (len(array1) ==0 or len(array2) == 0):
        print(-1)
        return
    else:
        i =0
        j=0
        while(True):
            if (i >= len(array1) or j >= len(array2)):
                return
            else:
                if (array1[i] == array2[j]):
                    print(array1[i],end=" ")
                    i+=1
                    j+=1
                else:
                    if(array1[i]>array2[j]):
                        # if (array2[j] not in copy1):
                            # print(array2[j],end=" ")
                        j+=1
                    else:
                        # if (array1[i] not in copy2):
                            # print(array1[i],end=" ")
                        i+=1
    print("")
    

num = int(input())
for i in range(num):
    n,m = (input()).split(" ")
    n = int(n)
    m = int(m)
    array1 = input().split(" ")
    array2 = input().split(" ")

    for j in range(n):
        array1[j] = int(array1[j])
    for j in range(m):
        array2[j] = int(array2[j])

    
    func(array1,array2)