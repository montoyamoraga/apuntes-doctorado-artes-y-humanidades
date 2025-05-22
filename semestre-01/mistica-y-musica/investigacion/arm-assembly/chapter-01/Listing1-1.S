// Listing1-1.S

// comentario

// .text directive tells Gas that the statements
// following this directive go in the section
// of memory reserced for machine instructions (code).

.text

// here is the main function
// it assumes the assembly language program
// is a standalone program with its own main function.

// on macOS the main program must have the name _main
// on Linux systems dont generally require the underscore.

// the .global _main statement makes the _main
// procedure's name visible outside this source file
// which is needed by the linker to produce an executable

.global _main, main

// the .align 2 statements tells the assembler to align
// the following code on a 4-byte boundary (required
// by the ARM CPU). The 2 operand specifies 2 raised
// to this power (2), which is 4.


.align 2

// here is the actual main program. it consists of a
// single ret (return) instruction that simply returns
// control to the operating system.

_main:
main:

  ret

