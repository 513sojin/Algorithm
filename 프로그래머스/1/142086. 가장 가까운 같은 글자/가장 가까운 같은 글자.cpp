#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    map<char,int> map;
    
    for(int i=0;i<s.size();i++){
        if(map.find(s[i])!=map.end()){
            answer.push_back(i - map[s[i]]);
            map[s[i]] = i;
        }else{
            answer.push_back(-1);
            map[s[i]] = i;
        }
    }
    
    return answer;
}