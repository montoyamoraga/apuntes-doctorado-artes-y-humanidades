// Listing1-2.S

// a simple C++ program that calls
// an assembly language function

// need to include stdio.h so this
// program can call printf()

#include <stdio.h>

// extern "C" namespace prevents
// "name mangling" by the C++
// compiler

extern "C" {
  // here is the external function
  // written in assembly language
  void asmMain(void);
};

int main(void) {
  printf("calling asmMain\n");
  asmMain();
  printf("returned from asmMain\n");
}