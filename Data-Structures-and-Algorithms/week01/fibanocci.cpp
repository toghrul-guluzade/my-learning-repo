#include <iostream>
#include <cmath>



int fibonacci(int k){

  if(k == 0) return 1;  // O(1)
  if(k == 1) return 1; // O(1)
  return fibonacci(k -1) + fibonacci(k - 2); //O(n) * O(n) == O(n^2) however it is exponential growth so it will timeout I don't know
}

int main(){
  int n;
  std::cin >> n;
  std::cout << fibonacci(n);

  return 0;
}