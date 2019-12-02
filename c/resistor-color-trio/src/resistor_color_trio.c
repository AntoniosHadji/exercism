#include "resistor_color_trio.h"
#include <math.h>

resistor_value_t color_code(resistor_band_t cc[]) {
  resistor_value_t result;

  result.value = (cc[0] * 10 + cc[1]) * (int) pow(10, cc[2]);

  if (result.value < 1000) {
    result.unit = OHMS;
  } else {
    result.unit = KILOOHMS;
    result.value /= KILOOHMS;
  }

  return result;
}


