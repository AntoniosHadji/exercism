#include <stdio.h>
#include <math.h>
#include "armstrong_numbers.h"

int isArmstrongNumber(int n) {
  int count = 1;
  // save original number
  int num = n;
  while (n > 9) {
    count += 1;
    n /= 10;
  }
  printf("count: %d ", count);

  // reset n to original num
  n = num;
  int sum = 0;
  if (n < 10) {
    sum = n;
  } else {
    for (int i=0; i < count; i++) {
      sum += pow(n % 10, count);
      n /= 10;
    }
  }
  printf("sum: %d ", sum);
  printf("num: %d\n", num);
  return sum == num;
}
