#include <iostream>

/*
Find the factorial of a number.

Input
One integer n (0≤n≤20).

Output
Print the value of n!=1⋅2⋅3⋅...⋅n.
*/

long long factorial(int i){
  if (i == 0){
    return 1;
  }
  return i * factorial(int(i-1));
}
int main(){
  int n;
  std::cin>>n;
  std::cout << factorial(n);

  return 0;
}