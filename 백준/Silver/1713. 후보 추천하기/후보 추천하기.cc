#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct info{
    int num, cnt, order;
};

bool compare_first(info a, info b){
    if(a.cnt == b.cnt) return a.order < b.order;
    
    return a.cnt < b.cnt;
}

bool compare_second(info a, info b){
    return a.num < b.num;
}

int main(){
    int frame, count;
    cin >> frame;
    cin >> count;
    vector<info> v;
    int student[101] = {0,};
    
    for(int i=0;i<count;i++){
        int n;
        cin >> n;
        
        if(v.size()<frame) {
            if(student[n] == 1) {
                for(int k=0;k<v.size();k++){
                    if(v[k].num == n) {
                        v[k].cnt += 1;
                        break;
                    }
                }
            }
            else {
                v.push_back({n,1,i});
            }
        } else {
            if(student[n] == 1) {
                for(int k=0;k<v.size();k++){
                    if(v[k].num == n) {
                        v[k].cnt += 1;
                        break;
                    }
                }
            }
            else{
                sort(v.begin(), v.end(), compare_first);
                student[v[0].num] = 0;
                v[0] = {n,1,i};
            }
        }
        
        student[n] = 1;
    }
    
    sort(v.begin(), v.end(), compare_second);
    for(int i=0;i<v.size();i++){
        cout << v[i].num << " ";
    }
    cout << endl;
    
    return 0;
}
