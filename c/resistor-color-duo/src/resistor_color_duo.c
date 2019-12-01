#include "resistor_color_duo.h"



uint16_t color_code(resistor_band_t cc[]) {

  return cc[0] * 10 + cc[1];
}
