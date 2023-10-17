#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

int time_convert(string time) {
    
}

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    map<char, int> tmap;
    
    int int_today = stoi(today.substr(0,4)) * 12 * 28 + stoi(today.substr(5,2)) * 28 + stoi(today.substr(8,2));
    
    for(int i=0;i<terms.size();i++){
        stringstream ss(terms[i]);
        char alpha; int month;
        ss>>alpha>>month;
        tmap[alpha] = month*28;
    }
    
    for(int i=0;i<privacies.size();i++){
        string year = privacies[i].substr(0,4);
        string month = privacies[i].substr(5,2);
        string day = privacies[i].substr(8,2);
        char alp = privacies[i].back();
        
        int temp = stoi(year) * 12 * 28 + stoi(month) * 28 + stoi(day);
        if (int_today >= temp + tmap[alp]) {
            answer.push_back(i+1);
        }
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}