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

  // malloc requires free, which is called in test suite
  // https://en.cppreference.com/w/c/memory/malloc
  int length = 1;
  char *acronym = malloc(length * sizeof *acronym);

  acronym[0] = toupper(phrase[0]);

  int index = 1;

  while (*phrase++ != '\0') {
    if (isspace(*phrase) || *phrase == '-') {
      // realloc buffer to allow for additional character
      // https://en.cppreference.com/w/c/memory/realloc
      char *temp = realloc(acronym, ++length * sizeof *acronym);
      *acronym = *temp;
      acronym[index++] = toupper(*++phrase);
    }
  }

  return acronym;
}

