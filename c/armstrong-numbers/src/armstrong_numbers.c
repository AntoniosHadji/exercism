#include <math.h>
#include "armstrong_numbers.h"

int isArmstrongNumber(int n) {
  int count = 1;
  // save original number
  int num = n;
  // count number of digits
  while (n > 9) {
    count += 1;
    n /= 10;
  }

  // reset n to original num
  n = num;
  int sum = 0;
  for (int i=0; i < count; i++) {
    sum += pow(n % 10, count);
    n /= 10;
  }
  return sum == num;
}
