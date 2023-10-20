#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    string temp = "";
    
    for(int i=0;i<str.size();i++){
        if('A' <= str[i] && str[i] <= 'Z'){
            temp += str[i] + 32; 
        }else{
            temp += str[i] - 32;
        }
    }
    cout << temp;
    return 0;
}