#include "leap.h"

namespace leap {

  bool is_leap_year(int year) {
    bool four         = !(year % 4);
    bool hundred      = !(year % 100);
    bool four_hundred = !(year % 400);

    return (four && !hundred) || four_hundred;
  }
}
