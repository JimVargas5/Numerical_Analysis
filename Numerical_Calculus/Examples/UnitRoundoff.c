#include <math.h>
#include <stdio.h>

int
main(int argc, char *argv[])
{
  int k;
  double u;

  u=1.0;
  k=0;
  while(u+1.0>1.0){
    u*=0.5;
    k+=1;
  }
  printf("k=%d u=%.37e\n",k,u);

  return 0;
}