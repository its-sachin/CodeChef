def func(n):
    for i in n:
        if (int(i) != 7 and int(i) != 3):
            return "BETTER LUCK NEXT TIME"
    return "LUCKY"



num = int(input())
for i in range(num):
    n = (input())
    print(func(n))