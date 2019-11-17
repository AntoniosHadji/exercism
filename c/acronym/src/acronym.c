#include "acronym.h"
#include <stdlib.h>
// NULL in stdlib.h
#include <ctype.h>
// isspace
#include <string.h>

char *abbreviate(char *phrase) {
  if (phrase == NULL || !strcmp(phrase, "")) return NULL;

  char *acronym = malloc(50);

  int word_count = 0;
  acronym[0] = toupper(phrase[0]);
  int index = 1;

  while (*phrase++ != '\0') {
    if (isspace(*phrase) || *phrase == '-') {
      word_count++;
      acronym[index++] = toupper(*++phrase);
    }
  }

  return acronym;
}
