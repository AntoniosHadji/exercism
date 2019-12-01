#include "resistor_color_trio.h"
#include <math.h>


uint16_t color_code(resistor_band_t cc[]) {

  return (cc[0] * 10 + cc[1]) * (uint16_t) pow(10, cc[2]);
}
