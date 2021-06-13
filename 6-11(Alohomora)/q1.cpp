#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int power(long long x, unsigned int y, int p)
{
    int res = 1;     
    x = x % p; 
  
    if (x == 0) return 0;
 
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % p;
 
        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}

int main(int argc, char const *argv[])
{
    int N;
    cin>>N;

    for (int i=0; i<N; i++) {

        int n;
        cin>>n;
        if (n<4){
            cout<<0<<endl;
        }
        else{
            cout<<( (power(2,n,1000000007) -((2*(n+1))%1000000007))%1000000007)<<endl;
        }
    }
    return 0;
}
