#include "hamming.h"
#include <stdlib.h>
#include <string.h>

int compute(const char * lhs, const char * rhs)
{
  if (lhs == NULL || rhs == NULL || strlen(lhs) != strlen(rhs)) {
    return -1;
  }

  int result = 0;
  while (*lhs != '\0') {
    if (*lhs++ != *rhs++ ) {
      result++;
    }
  }

  return result;
}
