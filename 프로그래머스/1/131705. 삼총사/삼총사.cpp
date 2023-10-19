#include <string>
#include <vector>
#include <numeric>
#define MAX 13
using namespace std;

bool visited[MAX];
vector <int> temp;
int answer = 0;
void dfs(vector <int> &number, int idx) {
    if (temp.size() == 3){
        int sum = accumulate(temp.begin(), temp.end(),0);
        
        if(sum == 0){
            answer ++;
            return;
        }
    }
    
    for(int i=idx;i<number.size();i++){
        if(!visited[i]){
            visited[i] = 1;
            temp.push_back(number[i]);
            dfs(number, i + 1);
            visited[i] = 0;
            temp.pop_back();
        }
    }
}

int solution(vector<int> number) {
    dfs(number, 0);
    return answer;
}