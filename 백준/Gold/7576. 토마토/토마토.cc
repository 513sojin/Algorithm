#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
#define MAX 1001

struct tomato {
    int y,x,cnt;
};

int main(int argc, char** argv)
{
    int n,m;
    cin >> m >> n;
    int graph[MAX][MAX];
    queue<tomato> q;
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int k;
            cin >> k;
            graph[i][j] = k;
            
            if(k==1){
                q.push({i,j,0});
            }
        }
    }
    
    int dx[4] = {0,0,-1,1};
    int dy[4] = {-1,1,0,0};
    
    int x = 0, y = 0, cnt = 0;
    while (!q.empty()){
        x = q.front().x;
        y = q.front().y;
        cnt = q.front().cnt;
        q.pop();
        
        for(int i=0;i<4;i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            
            if(0<=ny && ny <n && 0<=nx && nx <m && graph[ny][nx] == 0){
                q.push({ny,nx,cnt+1});
                graph[ny][nx] = 1;
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(graph[i][j] == 0){
                cout << -1;
                return 0;
            }
        }
    }
    
    cout << cnt;
    return 0;
}
