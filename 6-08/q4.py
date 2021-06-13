from sys import maxsize
 
def func(array,n):
 
    ans = -maxsize - 1
    curr = 0
    i = 0
    j = 0
    s = 0
 
    for i in range(0,n):
 
        curr += int(array[i])
 
        if(ans < curr):
            ans = curr
            i = s
            j = i
 
        if(curr < 0):
            curr = 0
            s = i+1

    return ans

    
 

for _ in range(int(input())):
    n = int(input())
    array = input().split(" ")

    ans = func(array,n)
    if(ans<=0):
        print("Cannot study - ",ans)
    else:
        print("Can study - ",ans)