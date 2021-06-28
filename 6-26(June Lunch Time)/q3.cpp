#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        long long a,b;
        cin>>a>>b;
        if((b & (b-1))){
            cout<<"No"<<endl;
        }
        else{
            cout<<"Yes"<<endl;
        }
    }
    return 0;
}
