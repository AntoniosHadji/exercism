#include "word_count.h"
#include <string.h>
// strcmp
#include <ctype.h>
// isspace, ispunct, tolower

#include <stdio.h>

#define NEW_WORD_FOUND 77
#define NOT_A_WORD 88

int increment_word_index(char * word, word_count_word_t * words);

int word_count(const char * input_text, word_count_word_t * words) {
  // clear to start with a known value
  // this breaks the test, when added to tests all tests pass
  // memset(words, 0, sizeof(*words));
  int unique_words = 0;
  char current_word[MAX_WORD_LENGTH + 1] = {0};
  char c;  // current char
  int i = 0;

  // loop over input_text until end
  while ((c = tolower(*input_text++))) {
    // printf("c: [%c]\n", c);
    if (c == '\'') {
      char pre = (input_text-2)[0];
      char post = (input_text)[0];
      // test for if this c is part of a quoteed word
      if ((isspace(pre) && isalnum(post)) || (isalnum(pre) && isspace(post))) {
          continue;
      }
    }
    if (isalnum(c) || c == '\'') {
      //copy char to temp word
      if (strlen(current_word) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;
      current_word[i++] = c;
      // printf("current_word: %s\n", current_word);
    } else {
      // add or increment count
      int rc = increment_word_index(current_word, words);
      if (rc == EXCESSIVE_NUMBER_OF_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
      if (rc == NEW_WORD_FOUND) {
        unique_words++;
        printf("unique count: %d\n", unique_words);
      }
      memset(current_word, 0, sizeof(current_word));
      i = 0;
    }

  }
  current_word[i] = '\0';

  if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
    unique_words++;
  }

  //printf("pre-return unique count: %d\n", unique_words);
  return unique_words;
}

int increment_word_index(char * word, word_count_word_t * words) {
  //printf("increment_word_index: [%s]\n", word);
  // unsigned long
  // printf("length: [%lu]\n", strlen(word));
  if (*word == '\0') return NOT_A_WORD;

  // loop over array of structs
  for (int i=0; i<MAX_WORDS; i++) {
    // if word == text, found match, return index
    // printf("word: [%s] text: [%s] count: [%d]\n", word, words[i].text, words[i].count);
    if (strcmp(word, words[i].text) == 0) {
      // found word
      words[i].count++;
      return 1;  // not a new word
    }
    // if text is empty, end of word list
    if (*words[i].text == '\0') {
      // add new word
      for (int j = 0; j < MAX_WORD_LENGTH; j++) {
        words[i].text[j] = *word++;
      }
      words[i].count = 1;
      return NEW_WORD_FOUND;
    }
  }
  // did not find word in list, or empty space
  return EXCESSIVE_NUMBER_OF_WORDS;
}
