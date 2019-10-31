#include "darts.h"
#include <math.h>
#include <stdint.h>

#define RADIUS_OUTER 10
#define RADIUS_MIDDLE 5
#define RADIUS_INNER 1

uint8_t score(coordinate_t p) {
  double result = sqrt(pow(p.x, 2) + pow(p.y, 2));
  uint8_t score = 0;

  if (RADIUS_MIDDLE < result && result <= RADIUS_OUTER) {
    score += 1;
  } else if (RADIUS_INNER < result && result <= RADIUS_MIDDLE) {
    score += 5;
  } else if (result <= RADIUS_INNER) {
    score += 10;
  }

  return score;
}
