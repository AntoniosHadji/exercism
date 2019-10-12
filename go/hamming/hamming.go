package hamming

import "errors"

func Distance(a, b string) (int, error) {

  if len(a) != len(b) {
    return -1, errors.New("mismatch in string lengths");
  }

  result := 0;
  for i, _ := range a {
    // _ would be type rune
    // indexing into string returns a byte
    // a[i], b[i] are unicode code points, not actual text character
    if a[i] != b[i] {
      result += 1;
    }
  }

  return result, nil;
}
