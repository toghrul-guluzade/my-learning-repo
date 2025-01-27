#include <iostream>

long long sum_of_digits(long long n){
  if(n == 0){
    return 0;
  }
  return n % 10 + sum_of_digits(n / 10);
}

int main(){
  long long n;
  std::cin >> n;
  std::cout<<sum_of_digits(n);

  return 0;
}