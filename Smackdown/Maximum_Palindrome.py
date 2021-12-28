def ans(n):
    if(n==2):
        s='ab'
    elif(n==3):
        s = 'aba'
    elif(n%2==0):
        s = 'a'
        i = 0
        isa = False
        while i < (n//2) -2:
            if(isa):
                s+='aa'
            else:
                s += 'bb'
            isa = not isa
            i += 2

        s += s[::-1]
    else:
        s = 'a'
        i = 0
        isa = False
        while i < (n//2) - 2:
            if(isa):
                s+='aa'
            else:
                s += 'bb'
            isa = not isa
            i += 2

        s = s + 'a' + s[::-1]
    return s

def isPalindrome(s):
    return s == s[::-1]

for i in range(100):
    s = ans(i)
    print(s)
    c = 0
    for j in range(i):
        if(isPalindrome(s)):
            c += 1
        s = s[1:]+s[0]
    print(i,':',c)
# for _ in range(int(input())):
#     n = int(input())
#     print(ans(n))
    



