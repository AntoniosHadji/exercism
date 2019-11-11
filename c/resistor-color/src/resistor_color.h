#include <stdint.h>

#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

#define BLACK 0
#define BROWN 1
#define RED 2
#define ORANGE 3
#define YELLOW 4
#define GREEN 5
#define BLUE 6
#define VIOLET 7
#define GREY 8
#define WHITE 9

typedef int resistor_band_t;

resistor_band_t color_code(resistor_band_t color);
resistor_band_t* colors();

// must be static to be declared in header
static const resistor_band_t COLORS[] = {
  BLACK, BROWN, RED, ORANGE, YELLOW,
  GREEN, BLUE, VIOLET, GREY, WHITE
};

#endif
