#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char** argv){
  int x = 128;
  int y = 64;

  printf("x = %x\ny = %x\n", x, y);
  x = y ^ x;
  y = x ^ y;
  x = x ^ y;
  printf("x = %x\ny = %x\n", x, y);



  return 0;
}
