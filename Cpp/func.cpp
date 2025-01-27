#include <iostream>

int sum(int a, int b){
  return a + b;
}

int main(){

  int a, b;
  std::cout<<"Enter two numbers: ";
  std::cin>>a>>b;

  #ifdef __WIN32
    std::cout<<"The sum of " << a << " and " << b << " is: " << sum(a, b);
  #endif

  return 0;
}