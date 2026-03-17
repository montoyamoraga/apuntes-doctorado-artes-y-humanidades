#include "Pantalla.h"

// destructor
Pantalla::~Pantalla() {}

void Pantalla::configurar(uint8_t direccion) {

  for (int i = 0; i < Pantalla::columnas; i++) {
    Pantalla::lineaMostrar0 += " ";
    Pantalla::lineaMostrar1 += " ";
    Pantalla::lineaMostrar2 += " ";
    Pantalla::lineaMostrar3 += " ";
  }
  Pantalla::direccion = direccion;

  Pantalla::lcd.init();
  Pantalla::lcd.backlight();
  Pantalla::lcd.noAutoscroll();
  Pantalla::lcd.clear();
}

void Pantalla::cargarTexto(String nuevoTexto) {

  int numCaracteres = nuevoTexto.length();

  Pantalla::lineaMostrar1 = " ";
  Pantalla::lineaMostrar2 = " ";
  Pantalla::lineaMostrar3 = " ";

  if (numCaracteres < 20) {
    Pantalla::lineaMostrar0 = nuevoTexto.substring(0, numCaracteres);
  } else {
    Pantalla::lineaMostrar0 = nuevoTexto.substring(0, 0 + 20);

    if (numCaracteres < 40) {
      Pantalla::lineaMostrar1 = nuevoTexto.substring(20, numCaracteres);
    } else {
      Pantalla::lineaMostrar1 = nuevoTexto.substring(20, 20 + 20);

      if (numCaracteres < 60) {
        Pantalla::lineaMostrar2 = nuevoTexto.substring(40, numCaracteres);
      } else {
        Pantalla::lineaMostrar2 = nuevoTexto.substring(40, 40 + 20);
        if (numCaracteres < 80) {
          Pantalla::lineaMostrar3 = nuevoTexto.substring(60, numCaracteres);
        } else {
          Pantalla::lineaMostrar3 = nuevoTexto.substring(60, 40 + 20);
        }
      }
    }
  }
}

void Pantalla::mostrarMensaje() {

  Pantalla::lcd.setCursor(0, 0);
  Pantalla::lcd.print(
    Pantalla::lineaMostrar0);

  Pantalla::lcd.setCursor(0, 1);
  Pantalla::lcd.print(
    Pantalla::lineaMostrar1);

  Pantalla::lcd.setCursor(0, 2);
  Pantalla::lcd.print(
    Pantalla::lineaMostrar2);

  Pantalla::lcd.setCursor(0, 3);
  Pantalla::lcd.print(
    Pantalla::lineaMostrar3);
}

String Pantalla::rellenarConEspacios(String original) {
  String resultado = original.substring(0);
  while (original.length() <= Pantalla::columnas) {
    resultado = resultado + " ";
  }
  return resultado;
}

void Pantalla::moverDerecha() {
  Pantalla::lcd.scrollDisplayRight();
}

void Pantalla::moverIzquierda() {
  Pantalla::lcd.scrollDisplayLeft();
}