for _ in range(int(input())):

    n = int(input())
    a = input().split()
    b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))


    diff = ord(a[0])-ord(b[0])
    done =False
    i = 1
    while(i<n):
        c = ord(a[i])-ord(b[i])
        if(c!=diff):
            print("NO")
            done =True
            break
        i+=1
    if (done==False):
        print("YES")

