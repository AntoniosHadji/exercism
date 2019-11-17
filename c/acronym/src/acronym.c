#include "acronym.h"
#include <stdlib.h>
// NULL in stdlib.h
#include <ctype.h>
// isspace
#include <stdio.h>
// printf


char *abbreviate(char *phrase) {
  if (phrase == NULL) return NULL;

  char *acronym = malloc(50);

  int word_count = 0;
  acronym[0] = phrase[0];
  int index = 1;

  while (*phrase != '\0') {
    //printf("%s\n", phrase);
    if (isspace(*phrase++)) {
      //printf("found space\n");
      word_count++;
      //printf("words: %d\n", word_count);
      // printf("acronym: %s\n", acronym);
      acronym[index++] = toupper(phrase[0]);
      // printf("acronym: %s\n", acronym);
    }
  }

  return acronym;
}
