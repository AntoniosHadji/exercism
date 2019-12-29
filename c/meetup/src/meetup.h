#ifndef MEETUP_H
#define MEETUP_H

#include <stdbool.h>

int meetup_day_of_month(
    unsigned int,
    unsigned int,
    const char *,
    const char *
    );

int day_string_to_int(const char * );
bool is_leap_year(unsigned int);
int days_in_month(unsigned int , unsigned int );
#endif
