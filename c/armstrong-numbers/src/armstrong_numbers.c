#include <stdio.h>
#include <math.h>
#include "armstrong_numbers.h"

int isArmstrongNumber(int n) {
  int count = 1;
  // create working variable equal to n
  int num = n;
  // count number of digits
  while (num > 9) {
    count += 1;
    num /= 10;
  }
  // reset working variable to original n
  num = n;
  int sum = 0;
  for (int i=0; i < count; i++) {
    sum += pow(num % 10, count);
    num /= 10;
  }
  return sum == n;
}
