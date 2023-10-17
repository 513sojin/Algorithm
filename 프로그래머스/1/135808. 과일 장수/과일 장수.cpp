#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int i, int j) { return i > j;}

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    sort(score.begin(), score.end(), compare);
    
    int length = score.size() / m;
    
    for(int i=0;i<length;i++){
        vector<int> v(score.begin()+i*m, score.begin()+(i+1)*m);
        answer += v[v.size()-1] * m;
    }
    return answer;
}