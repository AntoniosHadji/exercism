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
  //char current_word[MAX_WORD_LENGTH + 1] = {0};
  //  char c;
  //  int i = 0;
  // create temp input because strtok is destructive
  int input_length = strlen(input_text);
  char temp_input[input_length];
  strncpy(temp_input, input_text, input_length);

  char * delim = " :,!&@$%^&.\n";
  char *token = strtok(temp_input, delim);
  while(token) {
    puts(token);
    // return if EXCESSIVE_LENGTH_WORD
    if (strlen(token) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;
    // return if MAX_WORDS already found
    if (unique_words == MAX_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;

    unique_words += increment_word_index(token, words);

    token = strtok(NULL, delim);
  }

//  // loop over input_text until end
//  while ((c = tolower(*input_text++))) {
//    // return if EXCESSIVE_LENGTH_WORD
//    if (strlen(current_word) > MAX_WORD_LENGTH) return EXCESSIVE_LENGTH_WORD;
//    // return if MAX_WORDS already found
//    if (unique_words == MAX_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
//
//    // if c is alphanumeric, or apostrophe
//    if (isalnum(c) || c == '\'') {
//      //add char to current word
//      current_word[i++] = c;
//    }
//
//    // c is a word boundary character, or finished with input_text
//    if ((!isalnum(c) && c != '\'') || *input_text == '\0') {
//      if (*current_word != '\0') {
//        // count word if new, or increment existing word
//        unique_words += increment_word_index(current_word, words);
//        // reset variables for next word
//        memset(current_word, 0, sizeof(current_word));
//        i = 0;
//      }
//    }
//  }

  return unique_words;
}

char * strip_quotes(char * word) {
  int length = strlen(word);
  // are there quotes around word? if so, strip
  if (*word == '\'' && *(word+(--length)) == '\'') {
    // move pointer to next char
    word++;
    // remove last char
    word[--length] = '\0';
  }
  return word;
}

int increment_word_index(char * word, word_count_word_t * words) {
  word = strip_quotes(word);
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
  // if strlen <= 0 no word, return and do not increment any word
  return 0;
}
