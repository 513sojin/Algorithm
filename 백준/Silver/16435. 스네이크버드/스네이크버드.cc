#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N,L;
    cin >> N >> L;
    
    vector<int>v(N);
     
    for(int i=0; i<N; i++){
        cin>>v[i];
    }
    
    sort(v.begin(), v.end());
    
    for(int i=0; i<N; i++){
        if(v[i]<=L)
            L+=1;
    }
    
    cout << L << "\n";
    
    return 0;
}
