#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


int main() {
    int n1, n2;
    string order1, order2;
    cin >> n1 >> n2;
    
    vector<pair<char, int>> v;
    string str;
    cin >> str;
    
    for(int i = n1-1; i >= 0;i--){
        v.push_back(make_pair(str[i], 0));
    }
    
    cin >> str;
    for(int i=0;i<n2;i++){
        v.push_back(make_pair(str[i],1));
    }
    
    int t;
    cin >> t;
    int time = 0;
    
    while(time!=t){
        for(int i=0;i<n1+n2-1;i++){
            if(v[i].second == 0 && v[i+1].second == 1){
                swap(v[i], v[i+1]);
                i++;
            }
        }
        time ++;
    }
    
    for(int i=0;i<n1+n2;i++){
        cout<<v[i].first;
    }
}
