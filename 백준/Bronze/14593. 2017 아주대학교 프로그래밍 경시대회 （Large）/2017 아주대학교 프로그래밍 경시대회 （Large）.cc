#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct score{
    int s,c,l,o;
};

bool compare(score a, score b){
    if(a.s == b.s && a.c == b.c) return a.l < b.l;
    if(a.s == b.s) return a.c < b.c;
    
    return a.s > b.s;
}

int main(){
    int n;
    cin >> n;
    vector<score> v;
    
    for(int i=1;i<=n;i++){
        int s,c,l;
        cin >> s >> c >> l;
        v.push_back({s,c,l,i});
    }
    
    sort(v.begin(), v.end(), compare);
    cout << v[0].o << endl;
    
    return 0;
}
