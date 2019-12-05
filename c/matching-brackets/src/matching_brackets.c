#include "matching_brackets.h"

bool is_paired(const char *input) {
  // declare char to hold current character
  char c;
  // track last opened bracket
  char sequence[10] = {0};
  int index = 0;
  // loop through all input
  while ((c = *input++)) {
    // add opening brackets to sequence
    if (c == '(' || c == '[' || c == '{') {
      sequence[index++] = c;
    }

    // test if last opened bracket matches this closing bracket
    switch (c) {
    case ')':
      if (sequence[index-1] == '(') {
        index--;
        break;
      }
      // out of order return false
      return false;
    case ']':
      if (sequence[index-1] == '[') {
        index--;
        break;
      }
      // out of order return false
      return false;
    case '}':
      if (sequence[index-1] == '{') {
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
