#ifndef PANTALLA_H
#define PANTALLA_H

#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

class Pantalla {

private:
  LiquidCrystal_I2C lcd;

public:
  // constructor
  Pantalla(uint8_t direccion, int columnas, int filas)
    : lcd(direccion, columnas, filas) {}

  // destructor
  ~Pantalla();

  void configurar(uint8_t direccion);

  void cargarTexto(String nuevoTexto);

  void mostrarMensaje();

  String rellenarConEspacios(String original);

  void moverDerecha();
  void moverIzquierda();

  uint8_t direccion = 0x25;
  int columnas = 20;
  int filas = 4;

  String lineaMostrar0 = "";
  String lineaMostrar1 = "";
  String lineaMostrar2 = "";
  String lineaMostrar3 = "";

  String linea0 = "";
  String linea1 = "";
  String linea2 = "";
  String linea3 = "";

  int pos0 = 0;
  int pos1 = 0;
  int pos2 = 0;
  int pos3 = 0;

  int pausa = 10;
};

#endif