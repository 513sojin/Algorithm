#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    map<string, int> m1;
    // vector<string> answer(players);
    
    for (int i = 0; i<players.size(); i++) {
        m1[players[i]] = i;
    }
    
    for(int i=0;i<callings.size();i++){
        int locate = m1[callings[i]];
        m1[players[locate-1]] +=1;
        m1[callings[i]] -=1;
        // answer에 저장된 순서 변경
        string tmp = players[locate];
        players[locate] = players[locate-1];
        players[locate-1] = tmp; 
    }
    
    return players;
}