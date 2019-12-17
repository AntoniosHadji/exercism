#include "grains.h"
#include <math.h>
#include <stdio.h>

uint64_t square(uint8_t index) {
  if (0 < index && index < 65) {
    // ull = unsigned long long c standard is 64 bits
    // bit shifting 1 is same as 2 to same power
    return 1ull<<(index - 1);
  }
  return 0;
}

uint64_t total(void) {
  uint64_t t = 0;
  for (int i = 1; i < 65; i++) {
    t += square(i);
  }
  return t;
}
