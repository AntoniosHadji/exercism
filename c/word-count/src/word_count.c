#include "word_count.h"

int word_count(const char *input_text, word_count_word_t * words) {
  int unique_words = 0;
  words[0].count = 1;

  for (int i = 0; i < MAX_WORD_LENGTH; i++) {
    words[0].text[i] = *input_text++;
  }

  return unique_words + 1;
}


