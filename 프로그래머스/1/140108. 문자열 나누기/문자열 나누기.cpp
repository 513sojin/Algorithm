#include <string>
#include <vector>
#include <iostream>

using namespace std;

int count = 0;

void recursion(string words) {
    if (words.empty()) return;
    
    char first = words[0];
    int same = 1; int diff = 0;
    
    string temp = words.substr(1);
    
    for(int i=0;i<temp.size();i++){
        if(same==diff){
            count ++;
            recursion(temp.substr(i));
            return;
        }
        
        if (first == temp[i]) same ++;
        else diff ++;
    }
    
    count ++;
}

int solution(string s) {
    recursion(s);
    return count;
}