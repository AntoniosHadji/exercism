#include <stdio.h>
#include <stddef.h>
#include "hello_world.h"

void hello(char *buffer, const char *name)
{
  // set default greeting and name
  char greeting[] = "Hello, ";
  char defaultName[] = "World";

  short j = 0;
  short i = -1; // -1 because incrementer is before first use
  while (greeting[++i] != '\0') {
    buffer[i] = greeting[i];
  }

  if (name == NULL)
  {
    // if name is NULL buffer is default value
    while (defaultName[j] != '\0') {
      buffer[i++] = defaultName[j++];
    }
  }
  else
  {
    // if name is NOT NULL, insert name into buffer message
    while (name[j] != '\0') {
      buffer[i++] = name[j++];
    }
  }

  buffer[i] = '!';
  buffer[++i] = '\0';
}

// best answer found is only one line
// sprintf function takes same arguments as this hello function
// sprintf(buffer, "Hello, %s!", (name) ? name : "World");
//
// For next learning, make sure to review all headers included in stub file
