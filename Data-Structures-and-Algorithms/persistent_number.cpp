#include <iostream>

long long p(long long x){
  if(x < 10){
    return x;
  }
  return x % 10 * p(x/10);

}

int main(){
  long long a;

  while( std::cin>>a){

    int cnt = 0;
    while (a >= 10){
      a = p(a);
      cnt++;
    }

    std::cout<<cnt<<"\n";

  }

  return 0;
}