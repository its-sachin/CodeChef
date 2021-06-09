def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


def func(changes,s,n,k):

    d = 0
    for i in range(n):
        if (i!= n-1):
            if (s[i] == s[i+1]):
                d+=2
            else:
                d+=1

    if (n==1):
        for j in changes:
            print(d)
    else:
        for j in changes:
            
            i = int(j)-1
            if (i==0):
                if (s[i] == s[i+1]):
                    d-=1
                else:
                    d+=1
            elif(i==n-1):
                if (s[i] == s[i-1]):
                    d-=1
                else:
                    d+=1
            else:
                if (s[i] == s[i-1]):
                    if(s[i] == s[i+1]):
                        d-=2
                else:
                    if (s[i] != s[i+1]):
                        d+=2

            if (s[i]=='1'):
                s[i]='0'
            else:
                s[i]='1'
            print(d)

def main(num):

    for i in range(num):
        n,k = (input()).split(" ")
        n,k = int(n),int(k)
        s = input()
        s=Convert(s)
        changes = input().split(" ")
        func(changes,s,n,k)


try:

   num = int(input())
   main(num)

except:

   pass
