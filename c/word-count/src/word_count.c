#include "word_count.h"
#include <string.h>
// strcmp
#include <ctype.h>
// isspace, ispunct, tolower

#include <stdio.h>

#define NEW_WORD_FOUND 1

int increment_word_index(char * , word_count_word_t * );
void clear_array(word_count_word_t * );

int word_count(const char * input_text, word_count_word_t * words) {
  // clear to start with a known value
  clear_array(words);

  int unique_words = 0;
  char current_word[MAX_WORD_LENGTH + 1] = {0};
  char c;
  int i = 0;

  // loop over input_text until end
  while ((c = tolower(*input_text++))) {
    // return if EXCESSIVE_LENGTH_WORD
    if (strlen(current_word) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;

    // test if this c is part of a quoted word, if so skip quotes
    if (c == '\'') {
      char pre = (input_text-2)[0];
      char post = (input_text)[0];
      // previous character is space, next char is alphanumeric == opening quote
      // previos character is alphanumeric, next char is space == closing  quote
      if ((isspace(pre) && isalnum(post)) || (isalnum(pre) && isspace(post))) {
          continue;
      }
    }

    if (isalnum(c) || c == '\'') {
      if (unique_words == MAX_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
      //copy char to temp word
      current_word[i++] = c;
    } else {
      // count word
      if (*current_word != '\0') {
        unique_words += increment_word_index(current_word, words);
      }

      memset(current_word, 0, sizeof(current_word));
      i = 0;
    }
  }

  if (*current_word != '\0') {
      unique_words += increment_word_index(current_word, words);
  }

  return unique_words;
}

void clear_array(word_count_word_t * words) {
  for (int i=0; i<MAX_WORDS; i++) {
    strncpy(words[i].text, "\0", MAX_WORD_LENGTH);
    words[i].count = 0;
  }
}

int increment_word_index(char * word, word_count_word_t * words) {
  // loop over array of structs
  for (int i=0; i<MAX_WORDS; i++) {
    // if word == text, found match, return index
    if (strcmp(word, words[i].text) == 0) {
      // found word
      words[i].count++;
      return 0;  // did not find a new word
    }
    // if text is empty, end of word list, add new word if word not empty
    if (*words[i].text == '\0') {
      strncpy(words[i].text, word, MAX_WORD_LENGTH);
      words[i].count = 1;
      return 1;  // found new word
    }
  }
  // this should never be reached
  return 1000;
}
