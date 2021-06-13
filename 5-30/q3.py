def func(person,n,m,k):
    out = []
    for i in range(n):
        out.append(0)
    for i in person:
        if (i<=n):
            out[i-1]+=1
    ans = []
    for i in range(n):
        if (out[i] > 1):
            ans.append(i+1)
    return ans

num = int(input())

for i in range(num):

    n,m,k = (input()).split(" ")
    n,m,k = int(n),int(m),int(k)
    person = input().split(" ")

    for j in range(k):
        person[j] = int(person[j])

    ans = func(person,n,m,k)

    print(len(ans),end = " ")
    for i in ans:
        print(i, end = " ")
    print()
