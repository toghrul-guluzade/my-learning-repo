#include <iostream>


long long f(long long a, long long b){
  if(a == 0) return b;
  if(b == 0) return a;
  if(a >= b){
    return f(a % b, b);
  } else if(a < b){
    return f(b % a, a);
  }
}


int main(){
  long long a, b;
  std::cin>>a>>b;

  std::cout<<f(a, b);


  return 0;
}