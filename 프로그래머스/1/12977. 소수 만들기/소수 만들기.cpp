#include <vector>
#include <iostream>
#include <math.h>
using namespace std;

vector<int> temp(3,0);    
int answer = 0;

bool check_prime(int num){
    for(int i=2;i<=sqrt(num);i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}

void backtracking(vector<int> &nums, int index, int depth){
    if (depth == 3) {
        int sum = temp[0] + temp[1] + temp[2];
        if(check_prime(sum)){
            answer += 1;
        }
        return;
    }
    else {
        for(int i = index; i<nums.size();i++){
            temp[depth] = nums[i];
            backtracking(nums, i+1, depth+1);
        }      
    }
}

int solution(vector<int> nums) {
    backtracking(nums, 0, 0);
    return answer;
}