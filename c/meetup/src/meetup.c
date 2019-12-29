#include "meetup.h"
#include <string.h>
#include <time.h>
// bool is a macro for _Bool, as are true & false
#include <stdbool.h>
// see https://en.wikipedia.org/wiki/Zeller%27s_congruence for alternative method


int meetup_day_of_month(
    unsigned int year,
    unsigned int month,
    const char *week,
    const char *day_of_week)
{
  int day_to_find = 0;
  int c = 0;
  struct tm start = {
    .tm_year=(year - 1900),
    .tm_mon=(month - 1),
  };

  day_to_find = day_string_to_int(day_of_week);

  if (strcmp("teenth", week) == 0) {
    start.tm_mday = 13;
  }
  if (strcmp("first", week) == 0) {
    start.tm_mday = 1;
  }
  if (strcmp("second", week) == 0) {
    start.tm_mday = 8;
  }
  if (strcmp("third", week) == 0) {
    start.tm_mday = 15;
  }
  if (strcmp("fourth", week) == 0) {
    start.tm_mday = 22;
  }
  if (strcmp("fifth", week) == 0) {
    // TODO: Does this work for all edge cases?
    if (month == 2 && !is_leap_year(year)) return 0;
    start.tm_mday = 29;
  }
  if (strcmp("last", week) == 0) {
    start.tm_mday = days_in_month(month, year);
    mktime(&start);
    c = (start.tm_wday - day_to_find);
    start.tm_mday -= c < 0 ? 7 + c: c;
    return start.tm_mday;
  }

  mktime(&start);
  c = (day_to_find - start.tm_wday);
  start.tm_mday += c < 0 ? 7 + c: c;
  return start.tm_mday;
}

int day_string_to_int(const char * day_of_week) {
    if (strcmp("Monday", day_of_week) == 0) {
      return 1;
    }
    if (strcmp("Tuesday", day_of_week) == 0) {
      return 2;
    }
    if (strcmp("Wednesday", day_of_week) == 0) {
      return 3;
    }
    if (strcmp("Thursday", day_of_week) == 0) {
      return 4;
    }
    if (strcmp("Friday", day_of_week) == 0) {
      return 5;
    }
    if (strcmp("Saturday", day_of_week) == 0) {
      return 6;
    }
    if (strcmp("Sunday", day_of_week) == 0) {
      return 0;
    }
    // error value, string did not match any weekday
    return -1;
}

bool is_leap_year(unsigned int year) {
  // divisible by 4
  bool four         = !(year % 4);
  // divisible by 100
  bool hundred      = !(year % 100);
  // divisible by 400
  bool four_hundred = !(year % 400);

  return (four && !hundred) || four_hundred;
}

int days_in_month(unsigned int month, unsigned int year)
{
  switch(month) {
      case 1 : return 31;
      case 2 : return is_leap_year(year) ? 29 : 28;
      case 3 : return 31;
      case 4 : return 30;
      case 5 : return 31;
      case 6 : return 30;
      case 7 : return 31;
      case 8 : return 31;
      case 9 : return 30;
      case 10 : return 31;
      case 11 : return 30;
      case 12 : return 31;
  }
  return 0;
}
