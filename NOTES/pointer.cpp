#include <iostream>


int main(){

  int a = 1025 ;
  int *p;
  p = &a;
  char *p0;

  p0 = (char*)p;

  printf("%d", *p0);


  return  0;
}