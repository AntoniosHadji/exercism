#include "gigasecond.h"
#include <math.h>

time_t gigasecond_after(time_t d)
{
  return d + pow(10, 9);
}


