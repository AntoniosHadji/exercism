#include "matching_brackets.h"

// defined placeholders for characters to be matched
#define OP '('
#define CP ')'
#define OS '['
#define CS ']'
#define OB '{'
#define CB '}'
#define SQUARE 0
#define BRACE 1
#define PAREN 2

bool is_paired(const char *input) {
  // declare char to hold current character
  char c;
  // track last opened bracket
  char sequence[50] = {0};
  int index = 0;
  // create tracking array to count (,),[,],{,}
  int counter[3] = {0};
  // loop through all input
  while ((c = *input++)) {
    switch (c) {
    case OS:
      counter[SQUARE] += 1;
      sequence[index++] = OS;
      break;
    case CS:
      if (counter[SQUARE] > 0 && sequence[index-1] == OS) {
        counter[SQUARE] -= 1;
        index--;
      } else {
        // out of order return false
        return false;
      }
      break;
    case OB:
      counter[BRACE] += 1;
      sequence[index++] = OB;
      break;
    case CB:
      if (counter[BRACE] > 0 && sequence[index-1] == OB) {
        counter[BRACE] -= 1;
        index--;
      } else {
        // out of order return false
        return false;
      }
      break;
    case OP:
      counter[PAREN] += 1;
      sequence[index++] = OP;
      break;
    case CP:
      if (counter[PAREN] > 0 && sequence[index-1] == OP) {
        counter[PAREN] -= 1;
        index--;
      } else {
        // out of order return false
        return false;
      }
      break;
    }

  }
  int result = 0;
  for (int x = 0; x < 3; x++) {
    result += counter[x];
  }
  // return false if there is a missing pair
  return result == 0;
}
