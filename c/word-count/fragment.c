#include "src/word_count.h"
#include <stdio.h>
//       // without subscript, returns whole string
//       // -1, +1 give previous/next array value via pointer
// input_text is pointer to char
//       printf("prior:c:next => [%c]:[%c]:[%c]\n", (input_text-1)[0], c, (input_text+1)[0]);

//  this works in test, not in function
// memset(actual_solution, 0, sizeof(actual_solution));     // clear to start with a known value

//printf("pre-return unique count: %d\n", unique_words);
//for (int i=0; i<MAX_WORDS; i++) {
//  printf("text: [%s] count: [%d]\n", words[i].text, words[i].count);
//}



// experimentation with sizeof
void show_size(word_count_word_t * words) {
  unsigned long total_size = 0;
  for (int i=0; i<MAX_WORDS; i++) {
    unsigned long x = sizeof words[i];
    printf("sizeof: %lu\n", x);
    total_size += x;
  }
  printf("total: %lu\n", total_size);
  printf("int: %lu\n", sizeof(int));
  printf("char array: %lu\n", sizeof(char[MAX_WORD_LENGTH + 1]));

}

// sizeof: 56  alignment to multiple of 8? or +1 for ?
// sizeof: 56
// total: 1120
// int: 4
// char array: 51  total sizeof = 55
