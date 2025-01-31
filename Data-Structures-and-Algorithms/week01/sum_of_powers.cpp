#include <iostream>
#include <cmath>

long long pow_sum(long long base, long long exponent, long long modulus){
  if(exponent == 0) return 1;
  if(exponent % 2 == 0){
    long long half = pow_sum(base, exponent / 2, modulus);
    return (half * half) % modulus;
  } else 
return (base * pow_sum(base, exponent - 1, modulus)) % modulus;
  
}

// k * (k+1)^n

// 1^n + 2^n + 2 * 3^n .....) % m 
int main(){
  long long exponent, modulus;

  std::cin>>exponent>>modulus;


  long long sum = pow_sum(1, exponent, modulus) % modulus + pow_sum(2, exponent, modulus) % modulus;

  for(int base = 3; base <= 100; base++){
    sum = (sum + (base - 1) * pow_sum(base, exponent, modulus)) % modulus;
  }

  std::cout<<sum;


  return 0;
}