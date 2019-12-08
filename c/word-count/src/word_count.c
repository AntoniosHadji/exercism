#include "word_count.h"
#include <string.h>
// strcmp, strlen
#include <ctype.h>
// isspace, tolower, isalnum
#include <stdio.h>


int word_count(const char * input_text, word_count_word_t * words) {
  // clear to start with a known empty array
  memset(words, 0, MAX_WORDS * sizeof(word_count_word_t));
  int unique_words = 0;
  int input_length = strlen(input_text);
  char temp_input[input_length];
  // +1 to include \0
  strncpy(temp_input, input_text, input_length+1);

  char * delim = " :,!&@$%^&.\n\t";
  char *token = strtok(temp_input, delim);
  while(token) {
    // return if EXCESSIVE_LENGTH_WORD
    if (strlen(token) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;
    // return if MAX_WORDS already found
    if (unique_words == MAX_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
    // increment, or add word to index
    token = clean_word(token);
    unique_words += increment_word_index(token, words);
    // get next token
    token = strtok(NULL, delim);
  }

  return unique_words;
}

char * clean_word(char * word) {
  int length = strlen(word);
  // are there quotes around word? if so, strip
  if (*word == '\'' && *(word+(--length)) == '\'') {
    // move pointer to next char
    word++;
    // remove last char, length decremented a second time
    word[--length] = '\0';
  }
  // lower case the word
  for (int i = 0; i < length; i++) {
    word[i] = tolower(word[i]);
  }
  return word;
}

int increment_word_index(char * word, word_count_word_t * words) {
  for (int i=0; i<MAX_WORDS; i++) {
    // if word == text, found match, increment count
    if (strcmp(word, words[i].text) == 0) {
      // found word
      words[i].count++;
      return 0;  // did not find a new word
    }
    // if text is empty, end of word list, add new word
    if (*words[i].text == '\0') {
      strncpy(words[i].text, word, MAX_WORD_LENGTH);
      words[i].count = 1;
      return 1;  // found new word
    }
  }
  // return and do not increment word count
  return 0;
}
