#include <bits/stdc++.h>
using namespace std;
 
void add(vector<int> a[], int s, int d){
    a[s].push_back(d);
    a[d].push_back(s);
}
 
bool BFS(vector<int> adj[], int src, int dest, int v, int pred[], int dist[]){

    list<int> queue;
 
    bool visited[v];
 
    for (int i = 0; i < v; i++) {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }
 
    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);
 
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++) {
            if (visited[adj[u][i]] == false) {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);
 
                if (adj[u][i] == dest)
                    return true;
            }
        }
    }
 
    return false;
}
 
int ans(vector<int> adj[], int s, int dest, int v){

    int pred[v], dist[v];
 
    bool t = BFS(adj, s, dest, v, pred, dist);
    cout << dist[dest]<<endl;
 
}
 
int main(int argc, char const *argv[])
{
    int t;
    cin>>t;

    for (int i=0; i<t; i++){
        int m,n;
        cin>>m>>n;

        vector<int> adj[m*n];
        int a[m][n];

        for (int j=0; j<m; j++){
            for (int k=0; k<n; k++){
                int h;
                cin>>h;
                a[j][k] =h; 
            }
        }

        int xs,ys,xd,yd;
        cin>>xs>>ys>>xd>>yd;

        if (a[xs][ys] != a[xd][yd]){
            cout<<-1<<endl;
        }

        else{
            int c = a[xs][ys];

            for (int j=0; j<m; j++){
                for (int k=0; k<n; k++){
                    if (k!=0 && a[j][k-1] == c && a[j][k] == c){
                        add(adj,j*n+(k-1),j*n+k);
                    }
                    if (j!= 0 && a[j-1][k] == c && a[j][k] == c){
                        add(adj,(j-1)*n+k,j*n+k);
                    }
                }   
            }
            ans(adj,xs*n+ys,xd*n+yd,m*n);
        }
    }
    return 0;
}
