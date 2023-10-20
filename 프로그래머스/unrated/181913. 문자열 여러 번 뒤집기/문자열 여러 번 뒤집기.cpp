#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string my_string, vector<vector<int>> queries) {
    
    for(int i=0;i<queries.size();i++){
        int start = queries[i][0];
        int end = queries[i][1];
        
        string temp = "";
        for(int j = 0; j<= end-start;j++){
            temp += my_string[end-j];
        }
        my_string.replace(start, end-start + 1, temp);
    }
    
    return my_string;
}