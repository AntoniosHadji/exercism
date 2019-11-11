#include "resistor_color.h"
#include <stdint.h>

// constants can not be defined in header (unless static) because
// will cause multiple definition errors
// const resistor_band_t COLORS[] = {
//   BLACK, BROWN, RED, ORANGE, YELLOW,
//   GREEN, BLUE, VIOLET, GREY, WHITE
// };

resistor_band_t color_code(resistor_band_t color) {
  return color;
}

// returning array object is same as pointer to initial array element
// must cast to explicitly discard const qualifier
resistor_band_t* colors() {
  return  (resistor_band_t*) COLORS;
}
