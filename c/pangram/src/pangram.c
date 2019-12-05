#include "pangram.h"
#include <ctype.h>
#include <stdlib.h>

bool is_pangram(const char *sentence) {
  if (sentence == NULL) return false;

  char c;
  int alphabet[26] = {0};

  while ((c = tolower(*sentence++))) {
    if (isspace(c)) {
      continue;
    }
    alphabet[c - 97] += 1;
  }

  for (int i = 0; i < 26; i++) {
    if (alphabet[i] == 0) {
      return false;
    }
  }
  return true;
}
