def func(n):
    a = 1
    out = ""
    while(a<=n):
        out += str(a)
        print(out)
        j =0
        while(j<a):
            j+=1
            out+="*"
        a +=1



num = int(input())
for i in range(num):
    n = (input())
    print(func(n))