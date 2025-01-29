#include <iostream>
#include <cmath>



int fibonacci(int k){

  if(k == 0) return 1;  // O(1)
  if(k == 1) return 1; // O(1)
  return fibonacci(k -1) + fibonacci(k - 2);

int main(){
  int n;
  std::cin >> n;
  std::cout << fibonacci(n);

  return 0;
}