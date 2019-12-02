#include <stdint.h>

#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#define BLACK  0
#define BROWN  1
#define RED    2
#define ORANGE 3
#define YELLOW 4
#define GREEN  5
#define BLUE   6
#define VIOLET 7
#define GREY   8
#define WHITE  9

#define OHMS        1
#define KILOOHMS 1000

// Using int instead of uint16_t because values are greater than 2^16 (65536)
typedef int resistor_band_t;

typedef struct {
  int value;
  int unit;
} resistor_value_t ;


resistor_value_t color_code(resistor_band_t[]);
#endif


