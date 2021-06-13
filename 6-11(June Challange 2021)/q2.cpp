#include <iostream>

using namespace std;

void main(int argc, char const *argv[])
{
    int N;
    cin>>N;

    for (int i = 0; i < N; i++)
    {
        int D,d,P,Q;
        cin>>D>>d>>P>>Q;

        int k = D/d;
        int x = D - (k*d);
        int money = ((k*P + ((k-1)*k*Q)/2)*d + x*(P+k*Q));

        cout<<money<<endl;
    }

}
