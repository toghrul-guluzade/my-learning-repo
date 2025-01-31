#include <iostream>
#include <cmath>

const long long MOD = 1000000007;

long long pow_sum(long long base, long long exponent){
  if(exponent == 0) return 1;
  if(exponent % 2 == 0){
    long long half = pow_sum(base, exponent / 2);
    return (half * half) % MOD;
  } else 
return (base * pow_sum(base, exponent - 1)) % MOD;
  
}
int main(){
  long long n;

  std::cin>>n;
  
  long long ans = n * pow_sum(n-1, n-1) % MOD;
  std::cout<<ans;

  return 0;
}