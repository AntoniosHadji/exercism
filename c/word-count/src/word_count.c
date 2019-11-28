#include "word_count.h"
//#include <stdbool.h>
// true, false, bool type
#include <stdio.h>
// printf
#include <string.h>
// strcmp
#include <ctype.h>
// isspace, toupper, tolower

#define NEW_WORD_FOUND 77
#define NOT_A_WORD 88

int increment_word_index(char *word, word_count_word_t *words);

int word_count(const char *input_text, word_count_word_t * words) {
  // clear to start with a known value
  // this breaks the test
  // memset(words, 0, sizeof(*words));
  int unique_words = 0;
  char current_word[MAX_WORD_LENGTH + 1] = {0};
  char c;  // current char
  int i = 0;
  // loop over input_text until end
  while ((c = tolower(*input_text++))) {
    // test for end of word
    // printf("c: [%c]\n", c);
    if (isspace(c) || (ispunct(c) && c != '\'')) {
      // printf("tested for space or punc: [%c]\n", c);
      // add or increment count
      int rc = increment_word_index(current_word, words);
      if (rc == EXCESSIVE_NUMBER_OF_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
      if (rc == NEW_WORD_FOUND) {
        unique_words++;
        // printf("unique count: %d\n", unique_words);
      }
      memset(current_word, 0, sizeof(current_word));
      i = 0;
    } else {
      //copy char to temp word
      if (strlen(current_word) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;
      current_word[i++] = c;
      current_word[i] = '\0';
      // printf("current_word: %s\n", current_word);
    }
  }

  if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
    unique_words++;
  }

  return unique_words;
}

int increment_word_index(char *word, word_count_word_t *words) {
  //printf("increment_word_index: [%s]\n", word);
  //printf("increment_word_index: [%c]\n", *word);
  // unsigned long
  // printf("length: [%lu]\n", strlen(word));
  if (*word == '\0') return NOT_A_WORD;
  if (*word == '\'') {
    // word begins with apostrophe, assume quoted
    unsigned long i = 0;
    // shift word forward 1 char to overwrite first apostrophe
    // length - 2 to stop before last apostrophe
    for (; i < (strlen(word) - 2); i++) {
      word[i] = word[i+1];
    }
    // add new null to end string
    word[i] = '\0';
    // printf("increment_word_index post clean: [%s]\n", word);
  }

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
      // words[i].text[MAX_WORD_LENGTH + 1] = '\0';
      // printf("word: [%s] text: [%s] count: [%d]\n", word, words[i].text, words[i].count);
      return NEW_WORD_FOUND;
    }

    // printf("array[%d]: %s\n", i, words++->text);
  }
  // printf("word: %s\n", word);
  // did not find word in list, or empty space
  return EXCESSIVE_NUMBER_OF_WORDS;
}
