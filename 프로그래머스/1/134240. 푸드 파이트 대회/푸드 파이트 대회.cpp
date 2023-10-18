#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    string left_str = "";
    string right_str = "";
    
    for(int i=1;i<food.size();i++){
        int count = food[i] / 2;
        if (count <= 0) continue;
        
        for(int j=0;j<count;j++){
            left_str += to_string(i);
            right_str = to_string(i) + right_str;
        }
    }
    answer = left_str + "0" + right_str;
    
    return answer;
}