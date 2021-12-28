#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back



int main(int argc, char const *argv[])
{
    int MOD = 998244353;
    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){
        int n,m,d;
        cin >>n>>m>>d;
        int a[n];
        for (int i = 0; i < n; i++){
        
            a[i] = d;
        }
        
        for(int i=0; i<m; i++){
            int ci,bi;
            cin>>ci>>bi;
            a[ci-1] = min(a[ci-1],d/bi);
        }

        for (int i = n-2; i >= 0; i--){
            a[i] = min(a[i],a[i+1]);
        }
        
        vector<int> last;
        for(int i=0; i<a[n-1]; i++){
            if(i<a[0]){
                last.pb(1);
            }
            else{
                last.pb(0);
            }
        }

        for (int i = 1; i < n; i++){
        
            for(int j=1; j<a[i-1]; j++){
                last[j] = (last[j] + last[j-1])%MOD;
            }
            for (int j = a[i-1]; j < a[i]; j++){
                last[j] = last[a[i-1]-1];
            }

            for (int i = 0; i < a[n-1]; i++){
            
                cout<<last[i]<<" ";
            }
            cout<<endl;
        }
        int ans = 0;
        for (int i = 0; i < a[n-1]; i++){
            ans = (ans+last[i])%MOD;
        }
        cout << ans<<endl;
    }
    return 0;
}