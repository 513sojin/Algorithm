#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <string>
#define MAX 2000000000
using namespace std;

int solution(string s) {
    unordered_map<string, int> um;
    string number[11] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    
    for(int i=0;i<10;i++){
        um.insert({number[i], i});
    }
    
    for(pair<string,int> elem:um){
        int index = s.find(elem.first);
        while(index >= 0 && index <=MAX){
            s.replace(index, elem.first.size(), to_string(elem.second));
            index = s.find(elem.first);
        }
    }
    
    return stoi(s);
}