#include <iostream>
#include <cmath>
/*
Find the sum of the digits of the integer n.

Input
One 32-bit integer n (the number can be negative).

Output
Print the sum of the digits of the number n.
*/

long long sum_of_digits(long long n){
  if(n == 0){
    return 0;
  }
  return n % 10 + sum_of_digits(n / 10);
}

int main(){
  long long n;
  std::cin >> n;
  n = abs(n);
  std::cout<<sum_of_digits(n);

  return 0;
}