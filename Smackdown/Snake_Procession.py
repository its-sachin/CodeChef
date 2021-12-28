for _ in range(int(input())):
    n = int(input())
    s = input()

    a = 0
    invalid = False
    for i in range(n):
        if(s[i] == 'H'):
            a+=1
        elif(s[i]=='T'):
            a-=1

        if(a > 1 or a<0):
            invalid = True
            break
    
    if(a != 0):
        invalid = True
    if(invalid):
        print("Invalid")
    else:
        print('Valid')
    