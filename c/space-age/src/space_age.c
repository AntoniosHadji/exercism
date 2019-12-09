#include "space_age.h"


float convert_planet_age(planet_t planet, int64_t input)
{
  int seconds_in_earth_year = 31557600;
  // storage can not be placed in header?
  // this throws errors when placed in header, even if static is used
  float planets[] = {
       0.2408467,
       0.61519726,
       1,
       1.8808158,
       11.862615,
       29.447498,
       84.016846,
       164.79132
  };

  return (input / seconds_in_earth_year)  / planets[planet];
}
