

for _ in range(int(input())):

    n = int(input())

    if(n < 4):
        print(0)
    else:
        print( (pow(2,n,1000000007) -(2*(n+1))%1000000007)%1000000007)
    

