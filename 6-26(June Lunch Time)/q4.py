import math
def I():return input()
def II():return int(I())
def M():return map(int,I().split())
def L():return list(M())
def P(a):print(a)
for _ in range(II()):
    n,m,k = M()
    mat = [["n" for i in range(m+1)] for j in range(n+1)]
    win=0
    for i in range(m*n):
        x,y = M()
        
        if(win==0):
            if(i%2==0):
                mat[x][y]="a"

                
                if(x>=k and y>=k):
                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x-j][y-l] != "a"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=1

                if(win!=1 and x<=n-k+1 and y<=m-k+1):

                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x+j][y+l] != "a"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=1

                if(win!=1 and x<=n-k+1 and y>=k ):
                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x+j][y-l] != "a"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=1

                if(win!=1 and x>=k and y<=m-k+1):

                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x-j][y+l] != "a"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=1

                # if(win==1):
                #     print("win at",x,y)

                
            else:
                mat[x][y]="b"
                if(x>=k and y>=k):
                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x-j][y-l] != "b"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=-1

                if(win!=-1 and x<=n-k+1 and y<=m-k+1):

                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x+j][y+l] != "b"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=-1

                if(win!=-1 and x<=n-k+1 and y>=k ):
                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x+j][y-l] != "b"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=-1

                if(win!=-1 and x>=k and y<=m-k+1):

                    done =False
                    j=0
                    while(j<k and not done):
                        l=0
                        while(l<k and not done):
                            if(mat[x-j][y+l] != "b"):
                                done=True
                            l+=1
                        j+=1
                    if(not done):
                        win=-1

                # if(win==-1):
                #     print("win at",x,y)

            # print(mat)

    if(win==1):
        print("Alice")
    elif(win==-1):
        print("Bob")
    else:
        print("Draw")