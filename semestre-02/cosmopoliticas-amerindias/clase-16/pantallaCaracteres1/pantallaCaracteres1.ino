#include "Pantalla.h"
#include "Cunas.h"

// numeroArduino = 0
// 1: sin soldar
// 2: A0 soldada
// 3: A1 soldada

// numeroArduino = 1
// 4: sin soldar
// 5: A2 soldada

const uint8_t direccion1 = 0x27;
const uint8_t direccion2 = 0x26;
const uint8_t direccion3 = 0x25;
const uint8_t direccion4 = 0x27;
const uint8_t direccion5 = 0x23;

const int ancho = 20;
const int alto = 4;

Pantalla pantalla1 = Pantalla(direccion4, ancho, alto);
Pantalla pantalla2 = Pantalla(direccion5, ancho, alto);

Cunas cunas;

void setup() {
  pantalla1.configurar(direccion4);
  pantalla2.configurar(direccion5);
  pantalla1.cargarTexto(cunas.textos[3]);
  pantalla2.cargarTexto(cunas.textos[4]);
}

void loop() {
  pantalla1.mostrarMensaje();
  pantalla2.mostrarMensaje();
  // pausa en ms
  delay(700);
  pantalla1.moverDerecha();
  pantalla2.moverIzquierda();
}