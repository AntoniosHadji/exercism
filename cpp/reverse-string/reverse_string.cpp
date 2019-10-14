#include "reverse_string.h"
#include <string>
#include <algorithm>

namespace reverse_string {

  std::string reverse_string(std::string s) {
    reverse(begin(s), end(s));
    return s;
  }

}  // namespace reverse_string
