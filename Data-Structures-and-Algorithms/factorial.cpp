#include <iostream>

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