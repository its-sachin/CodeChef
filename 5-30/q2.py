def lang(i):
    if (ord(i) >= 97 and ord(i) <= 109):
        return 1
    elif (ord(i) >= 78 and ord(i) <= 90):
        return 2
    return 0


def func(sent):
    for i in sent:
        if (lang(i[0]) == 1):
            l = 1
        elif (lang(i[0]) == 2):
            l = 2
        else:
            return "NO"

        for j in i:
            if (lang(j) != l):
                return "NO" 

    return "YES"


num = int(input())

for i in range(num):

    sent = input().split(" ")
    k = sent[0]
    sent.remove(k)

    print(func(sent))
