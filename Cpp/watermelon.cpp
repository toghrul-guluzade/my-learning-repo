#include <iostream>


int main(){

  short int w;
  std::cin>>w;

  if(w >= 4 && w % 2 == 0){
    std::cout << "YES";
  } else {
    std::cout << "NO";
  }

  return 0;
}