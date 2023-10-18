#include <string>
#include <vector>

using namespace std;

bool visited[201];

void dfs(int i, int n, vector<vector<int>> computers){
    visited[i] = 1;
    
    for(int j=0;j<n;j++){
        if(!visited[j] && computers[i][j] == 1){
            dfs(j,n,computers);
        }
    }
    return;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(int i=0;i<n;i++){
        if(!visited[i]){
            dfs(i,n,computers);
            answer ++;
        }
    }
    return answer;
}