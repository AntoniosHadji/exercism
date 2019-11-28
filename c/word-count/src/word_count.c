#include "word_count.h"
#include <stdio.h>
// printf
#include <string.h>
// strcmp
#include <ctype.h>
// isspace

#define NEW_WORD_FOUND -77

int find_word_index(const char *word, word_count_word_t *words);
int increment_word_index(const char *word, word_count_word_t *words);

int word_count(const char *input_text, word_count_word_t * words) {
  int unique_words = 0;
//  int word_index = 0;
  char current_word[MAX_WORD_LENGTH + 1] = {0};
  char c;
  int i = 0;
  // loop over input_text until end
  while ((c = *input_text++)) {
    // test for end of word
    printf("c: %c\n", c);
    if (isspace(c)) {
      printf("tested for space or EOF: %c\n", c);
      // add or increment count
      if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
        unique_words++;
      }
      memset(current_word, 0, 1024);
    } else {
      //copy char to temp word
      current_word[i++] = c;
      current_word[i] = '\0';
      printf("%s\n", current_word);
    }
  }

  if (increment_word_index(current_word, words) == NEW_WORD_FOUND) {
    unique_words++;
  }

  printf("end\n");
  printf("%s\n", current_word);
  printf("c: [%c] (%d)\n", c, c);
  printf("c: [%c] (%d)\n", *input_text, *input_text);

  //for (; i < MAX_WORD_LENGTH; i++) {
  //  words[word_index].text[i] = *input_text++;
  //}
  //words[word_index].text[i] = '\0';
  //words[word_index].count = 1;
  //unique_words++;

  //word_index = find_word_index(input_text, words);
  //printf("next word index: %d\n", word_index);
  return unique_words;
}

int increment_word_index(const char *word, word_count_word_t *words) {
  printf("increment_word_index: %s\n", word);
  // loop over array of structs
  for (int i=0; i<MAX_WORDS; i++) {
    // if word == text, found match, return index
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
      return NEW_WORD_FOUND;
    }

    // printf("array[%d]: %s\n", i, words++->text);
  }
  // printf("word: %s\n", word);
  // did not find word in list, or empty space
  return EXCESSIVE_NUMBER_OF_WORDS;
}

int find_word_index(const char *word, word_count_word_t *words) {
  for (int i=0; i<MAX_WORDS; i++) {
    // if text is empty, end of word list
    if (*words->text == '\0') return i;

    // printf("array[%d]: %s\n", i, words++->text);
    // if word == text, found match, return index
    if (strcmp(word, words++->text) == 0) {
      return i;
    }
  }
  // printf("word: %s\n", word);
  // did not find word in list, or empty space
  return EXCESSIVE_NUMBER_OF_WORDS;
}

/* loop over *input_text
 * find space or end of string, this is end of 1 token
 */
