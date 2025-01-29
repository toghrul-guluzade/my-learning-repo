#include <iostream>
#include <cmath>
/*
Find the value of the expression x^n mod m.

Input
Three positive integers x,n,m (1 ≤ x, n ≤ 10^9, 2 ≤ m ≤ 10^9).

Output
Print the value of x^n mod m.
*/

long long f(int x, long long n, long long m){
  if(n == 0){
    return 1;
  }
  
  long long half = f(x, n/2, m);
  half = (half * half) % m;

  if(n % 2 != 0){
    half = (half * x) % m;
  }

  return half;
}


int main(){

  int x;
  long long n, m;

  std::cin >> x >> n >> m;
  std::cout << f(x, n, m);

  return 0;
}



/*
a^n = (a^2)^n/2 =


*/