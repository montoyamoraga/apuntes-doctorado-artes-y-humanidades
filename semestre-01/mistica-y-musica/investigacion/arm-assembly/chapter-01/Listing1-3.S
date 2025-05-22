// Listing1-3.S

// a simple Gas module that contains
// an empty function to be called by
// the C++ code in Listing1-2

.text

// here is the asmMain function

.global _asmMain, asmMain
.align 2

_asmMain:
asmMain:

  // empty function just returns to C++ code

  // returns to caller
  ret
