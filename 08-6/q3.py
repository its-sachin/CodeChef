# def isPrime(n) :
#     if (n < 2) :
#         return False
#     elif (n == 2 or n==3) :
#         return True
  
#     if (n % 2 == 0 or n % 3 == 0) :
#         return False
  
#     i = 5
#     while(i*i <= n) :
#         if (n%i == 0 or n%(i+2) == 0) :
#             return False
#         i += 6
  
#     return True

def tillPrime(n):
    i = 1
    primes = []
    count = 0

    while(count<n):

        if (i<5):
            i+=1
        else:
            i+=2
    
        if (i==2 or i==3):
            # print(" " ,i)
            count+=1
            primes.append(i)
        else:
            done = False
            for j in primes:
                if (i%j == 0):
                    done = True
                    break

            if (done == False):
                # print(" " ,i)
                count+=1
                primes.append(i)

                    
                    
    # print("c ",i)
    mod = i%4

    if (mod == 0):
        return i
    elif (mod == 1):
        return 1
    elif (mod == 2):
        return i+1
    return 0





for _ in range(int(input())):
    n = int(input())
    print(tillPrime(n))

