#include <string>
#include <vector>
#include <algorithm>
#define MAX 8

using namespace std;

int answer = 0;
bool visited[MAX] = {0};

void bfs(int cnt, int k, vector<vector<int>> dungeons) {
    if (cnt > answer) answer = cnt;
    
    for (int i = 0; i< dungeons.size(); i++) {
        if (dungeons[i][0] <= k && !visited[i]) {
            visited[i] = 1;
            bfs(cnt + 1, k - dungeons[i][1], dungeons);
            visited[i] = 0;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    bfs(0, k, dungeons);
    return answer;
}