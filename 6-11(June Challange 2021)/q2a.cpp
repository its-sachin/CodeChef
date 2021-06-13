#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    cin>>N;

    for (int j = 0; j < N; j++)
    {
        int D,d,P,Q;
        cin>>D>>d>>P>>Q;

        int rate = P;
        int i=0;
        int money = 0;

        while(i<D){
            money += rate;
            i+=1;
            if (i%d==0){
                rate+=Q;
            }
        }

        cout<<money<<endl;
    }
    


    return 0;
}
