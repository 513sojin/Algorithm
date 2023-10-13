#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    unordered_map<string, int> um;
    
    for (int i=0; i<name.size();i++) um[name[i]] = yearning[i];
    
    for (int i =0; i<photo.size();i++) {
        int count = 0;
        for (int j =0; j<photo[i].size();j++) {
            string person = photo[i][j];
            if (um.find(person) != um.end()) count += um[person];
        }
        answer.push_back(count);
    }
    return answer;
}