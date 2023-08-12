#include <stdio.h>

int main() { 
  long long n, sum = 0, s = 1;
  scanf("%lld",&n);

  while (n){
    if (n & 1){
      sum += s;
    }
    s *= 3;
    n >>= 1;
  }
  printf("%lld\n", sum);
  return 0;
}