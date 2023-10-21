#include <vector>
#include <iostream>
#include <queue>
#define MAX 100001
using namespace std;

bool visited[MAX];
vector<int> v[MAX];
int ans[MAX];

void bfs(){
    visited[1] = true;

    queue<int> q;
    q.push(1);

    while(!q.empty()) {
        int x = q.front();
        q.pop();

        for(int i=0;i<v[x].size();i++){
            int num = v[x][i];
            if(!visited[num]){
                q.push(num);
                visited[num] = true;
                ans[num] = x;
            }
        }
    }
}

int main(){
    int n;
    cin >> n;
    
    for(int i=0;i<n-1;i++){
        int x,y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    
    bfs();
    
    for(int i=2;i<=n;i++){
        cout << ans[i] << "\n";
    }
    
    return 0;
}