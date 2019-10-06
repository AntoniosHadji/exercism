#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool is_isogram(const char phrase[])
{
  int alphabet[26] = {0};
  int index;

  for (unsigned long i=0; i < strlen(phrase); i++) {
    if (phrase[i] == ' ' || phrase[i] == '-')
      continue;

    index = tolower(phrase[i]) - 'a';
    alphabet[index] += 1;
    if (alphabet[index] > 1) {
      return 0;
    }
  }

  return 1;
}

