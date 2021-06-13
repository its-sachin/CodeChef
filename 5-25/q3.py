
def func(array):

    if (len(array) == 1):
        return "YES"

    evenMax = -1
    oddMin = -1
    evenMin = -1
    oddMax = -1

    for i in array:
        if(i%2 == 0):
            if (evenMax == -1 or i > evenMax):
                evenMax = i
            if (evenMin == -1 or i < evenMin):
                evenMin = i
        else:
            if (oddMin == -1 or i < oddMin):
                oddMin = i
            if (oddMax == -1 or i > oddMax):
                oddMax = i
    
    if ((oddMin == -1 and oddMax == -1) or (evenMin == -1 and evenMax == -1) or (evenMax < oddMin or oddMax < evenMin)):
        return "YES"
    return "NO"



num = int(input())
for i in range(num):
    n = (input())
    n = int(n)
    array = input().split(" ")

    for j in range(n):
        array[j] = int(array[j])

    print("YES")