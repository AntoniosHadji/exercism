#include "acronym.h"
#include <stdlib.h>
// NULL in stdlib.h
#include <ctype.h>
// isspace in ctype.h

// reallocate buffer for return result instead of pre-calculating required length
// Why: uses only one loop instead of 2;

char *abbreviate(const char *phrase) {
  // '\0' == empty string
  if (phrase == NULL || *phrase == '\0') return NULL;

  // length will be at least 2 since phrase is not NULL or empty
  // min size = {char, \0}
  int length = 2;
  // calloc requires free, which is called in test suite
  // allocates memory on the heap, initialized to zeros
  // https://en.cppreference.com/w/c/memory/calloc
  char *acronym = calloc(length, sizeof(char));

  // set first character
  acronym[0] = toupper(phrase[0]);

  while (*phrase++ != '\0') {
    if (isspace(*phrase) || *phrase == '-') {
      // realloc buffer to allow for additional character
      // https://en.cppreference.com/w/c/memory/realloc
      acronym = realloc(acronym, ++length * sizeof(char));
      // length is now 2 more than next index spot
      // increment phrase before deference
      acronym[length - 2] = toupper(*++phrase);
    }
  }

  return acronym;
}

