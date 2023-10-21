#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
int parent[10001];

struct cruscal{
    int a, b, c;
};

bool compare(cruscal first, cruscal second){
    return first.c < second.c;
}

int find(int x){
    if(parent[x] == x) return x;
    else return parent[x] = find(parent[x]);
}

void union_find(int x,int y){
    x = find(x);
    y = find(y);
    parent[y] = x;
}

bool check_same_parent(int x, int y){
    x = find(x);
    y = find(y);
    if(x == y) return true; //부모가 같은 상태
    else return false;
}

int main(){
    int V,E;
    int result = 0;
    cin >> V >> E;
    vector<cruscal> v;
    
    for(int i=0;i<E;i++){
        int a,b,c;
        cin >> a >> b >> c;
        v.push_back({a,b,c});
    }
    
    sort(v.begin(),v.end(),compare);
    for(int i=1;i<=V;i++) parent[i] = i;
    for(int i=0;i<v.size();i++){
        if(!check_same_parent(v[i].a, v[i].b)){
            union_find(v[i].a, v[i].b);
            result += v[i].c;
        }
    }
    cout << result;
    return 0;
}
