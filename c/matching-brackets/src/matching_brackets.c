#include "matching_brackets.h"

// defined placeholders for characters to be matched
#define OP '('
#define CP ')'
#define OS '['
#define CS ']'
#define OB '{'
#define CB '}'

bool is_paired(const char *input) {
  // declare char to hold current character
  char c;
  // track last opened bracket
  char sequence[10] = {0};
  int index = 0;
  // loop through all input
  while ((c = *input++)) {
    // add opening brackets to sequence
    if (c == OS || c == OB || c == OP) {
      sequence[index++] = c;
    }

    // test if last opened bracket matches this closing bracket
    switch (c) {
    case CS:
      if (sequence[index-1] == OS) {
        index--;
        break;
      }
      // out of order return false
      return false;
    case CB:
      if (sequence[index-1] == OB) {
        index--;
        break;
      }
      // out of order return false
      return false;
    case CP:
      if (sequence[index-1] == OP) {
        index--;
        break;
      }
      // out of order return false
      return false;
    }
  }
  // if pairs are matched, index will equal zero
  return index == 0;
}
