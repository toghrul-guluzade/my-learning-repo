#include <iostream>
#include <cmath>

int digit_sum(int a){
  
  if(a == 0){
    return 0;
  }

  return a % 10 + digit_sum(a / 10);
}

int main(){

  int a, b;
  int min = 1000000;
  std::cin>> a >> b;
  int sum;

  for(int i = a; i <= b; i++){
    sum = digit_sum(i);
    if(sum < min){
      min = sum;
    }
  }
  
  int cnt = 0;

  for(int i = a; i <= b; i++){
    sum = digit_sum(i);
    if(sum == min){
      cnt++;
    }
  }
  std::cout<<cnt;

  return 0;
}