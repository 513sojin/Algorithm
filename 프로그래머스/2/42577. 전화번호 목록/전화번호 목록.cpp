#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

bool solution(vector<string> phone_book) {
    map<string,int> m;
    
    for(int i=0;i<phone_book.size();i++){
        m.insert(make_pair(phone_book[i],1));
    }
    
    for(int i=0;i<phone_book.size();i++){
        string temp = "";
        for(int j=0;j<phone_book[i].size();j++){
            temp += phone_book[i][j];
            
            if(m.find(temp)!=m.end() && temp != phone_book[i]) {
                return false;
            }
        }
    }
    
    return true;
}