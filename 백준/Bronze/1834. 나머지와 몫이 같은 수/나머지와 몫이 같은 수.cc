#include <iostream>

long long n;
long long sum = 0;

int main(int argc, char** argv){
  scanf("%lld", &n);

  for(long long i=1; i<n; i++){ // 나머지는 나누는 값을 넘을 수 없다
    sum += i*n + i;
  }

  printf("%lld\n", sum);

  return 0;
}