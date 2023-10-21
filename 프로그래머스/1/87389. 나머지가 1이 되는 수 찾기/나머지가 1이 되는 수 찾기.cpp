#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    if(n==1) return 0;
    if(n==2) return 1;
    
    for(int i=2;i<=n-1;i++) {
        if((n-1)%i==0) return i;
    }
    return answer;
}