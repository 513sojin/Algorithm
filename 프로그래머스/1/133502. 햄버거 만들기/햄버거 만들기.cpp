#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    stack<int> s;
    string temp = "";
    
    for(int i=0;i<ingredient.size();i++){
        temp += to_string(ingredient[i]);
        if (temp.size() >= 4 && temp.substr(temp.size()-4) == "1231") {
            answer += 1;
            temp = temp.substr(0,temp.size()-4);
        }
    }
    
    return answer;
}