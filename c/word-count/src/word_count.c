#include "word_count.h"
#include <stdio.h>
// printf
#include <string.h>
// strcmp
#include <ctype.h>
// isspace

#define NEW_WORD_FOUND -77

int increment_word_index(const char *word, word_count_word_t *words);

int word_count(const char *input_text, word_count_word_t * words) {
  // clear to start with a known value
  // this breaks the test
  // memset(words, 0, sizeof(*words));
  int unique_words = 0;
  char current_word[MAX_WORD_LENGTH + 1] = {0};
  char c;
  int i = 0;
  // loop over input_text until end
  while ((c = *input_text++)) {
    // test for end of word
    printf("c: [%c]\n", c);
    if (isspace(c) || ispunct(c)) {
      printf("tested for space or EOF: %c\n", c);
      // add or increment count
      if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
        unique_words++;
      }
      memset(current_word, 0, sizeof(current_word));
      i = 0;
    } else {
      //copy char to temp word
      current_word[i++] = c;
      current_word[i] = '\0';
      printf("current_word: %s\n", current_word);
    }
  }

  if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
    unique_words++;
  }

  return unique_words;
}

int increment_word_index(const char *word, word_count_word_t *words) {
  printf("increment_word_index: %s\n", word);
  // loop over array of structs
  for (int i=0; i<MAX_WORDS; i++) {
    // if word == text, found match, return index
    printf("word: %s text: %s\n", word, words[i].text);
    if (strcmp(word, words[i].text) == 0) {
      // found word
      words[i].count++;
      return i;
    }
    // if text is empty, end of word list
    if (*words[i].text == '\0') {
      // add new word
      for (int j = 0; j < MAX_WORD_LENGTH; j++) {
        words[i].text[j] = *word++;
      }
      words[i].count = 1;
      // words[i].text[MAX_WORD_LENGTH + 1] = '\0';
      printf("word: %s text: %s\n", word, words[i].text);
      return NEW_WORD_FOUND;
    }

    // printf("array[%d]: %s\n", i, words++->text);
  }
  // printf("word: %s\n", word);
  // did not find word in list, or empty space
  return EXCESSIVE_NUMBER_OF_WORDS;
}
