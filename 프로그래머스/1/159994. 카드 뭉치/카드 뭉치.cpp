#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "Yes";
    queue<string> first_q;
    queue<string> second_q;
    
    for (int i=0;i<cards1.size();i++) first_q.push(cards1[i]);
    for (int i=0;i<cards2.size();i++) second_q.push(cards2[i]);
    
    for (int i=0;i<goal.size();i++) {
        if (first_q.front() == goal[i]){
            first_q.pop();
        } else if (second_q.front() == goal[i]) {
            second_q.pop();
        } else {
            answer = "No";
        }
    }
    return answer;
}