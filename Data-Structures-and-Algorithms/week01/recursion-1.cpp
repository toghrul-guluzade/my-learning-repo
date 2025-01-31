#include <iostream>
/*
Implement the recursive function:
f(n)={ 
0,n=0
f(n−1)+n,n>0
}

Input
One integer n (0≤n≤1000).

Output
Print the value of f(n).

*/

int f(int n){
  if (n == 0){
    return 0;
  }
  return n + f(n - 1);
}

int main(){

  int n;
  std::cin>>n;
  std::cout<<f(n);

  return 0;
}