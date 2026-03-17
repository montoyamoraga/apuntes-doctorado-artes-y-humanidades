#ifndef CUNAS_H
#define CUNAS_H

#include <Arduino.h>

class Cunas {
public:
  Cunas();
  ~Cunas();
  String textos[5] = {
    "no",
    "hay",
    "naturaleza",
    "ni",
    "artificio",
  };
};

#endif