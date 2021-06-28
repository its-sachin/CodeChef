#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        string s;
        cin>>s;

        if(s[0]=='1'){
            cout<<s[0]<<0;
            for (int j=1;j<s.size();j++){
                cout<<s[j];
            }
        }
        else{
            cout<<1;
            for (int j=0;j<s.size();j++){
                cout<<s[j];
            }
        }
        cout<<""<<endl;
    }
    return 0;
}
