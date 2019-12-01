#include <stdint.h>

#ifndef RESISTOR_COLOR_DUO_H
#define RESISTOR_COLOR_DUO_H

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

typedef uint16_t resistor_band_t;

uint16_t color_code(resistor_band_t[]);

#endif

