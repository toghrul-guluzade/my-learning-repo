#include <iostream>

long long factorial(int i){
  if (i == 0){
    return 1;
  }
  return i * factorial(int(i-1));
}

int how_many(int n, int m){

  return factorial(n) / (factorial(n-m) * factorial(m));

}


int main(){

  int n, m;
  std::cin>>n>>m;

  std::cout<<how_many(n, m);
  return 0;
}