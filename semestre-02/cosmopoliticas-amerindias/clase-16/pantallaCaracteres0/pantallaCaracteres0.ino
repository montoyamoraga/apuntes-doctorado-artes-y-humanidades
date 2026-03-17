#include "Pantalla.h"
#include "Cunas.h"

// numeroArduino puede ser 1, 2
const int numeroArduino = 2;

// numeroArduino = 1
// 1: sin soldar
// 2: A0 soldada
// 3: A1 soldada

// numeroArduino = 2
// 4: sin soldar
// 5: A2 soldada

const uint8_t direccion1 = 0x27;
const uint8_t direccion2 = 0x26;
const uint8_t direccion3 = 0x25;
const uint8_t direccion4 = 0x27;
const uint8_t direccion5 = 0x23;

const int ancho = 20;
const int alto = 4;

Pantalla pantalla1 = new Pantalla();
Pantalla pantalla2;
Pantalla pantalla3;


Cunas cunas;

void setup() {

  if (numeroArduino == 1) {
    pantalla1 = Pantalla(direccion1, ancho, alto);
    pantalla2 = Pantalla(direccion2, ancho, alto);
    pantalla3 = Pantalla(direccion3, ancho, alto);

    pantalla1.configurar(direccion1);
    pantalla2.configurar(direccion2);
    pantalla3.configurar(direccion3);
    pantalla1.cargarTexto(cunas.textos[0]);
    pantalla2.cargarTexto(cunas.textos[1]);
    pantalla3.cargarTexto(cunas.textos[2]);
  } else if (numeroArduino == 2) {
    pantalla1 = Pantalla(direccion4, ancho, alto);
    pantalla2 = Pantalla(direccion5, ancho, alto);
    // pantalla3 = Pantalla(direccion3, ancho, alto);
    pantalla1.configurar(direccion4);
    pantalla2.configurar(direccion5);
    pantalla1.cargarTexto(cunas.textos[3]);
    pantalla2.cargarTexto(cunas.textos[4]);
  }
}

void loop() {
  if (numeroArduino == 1) {
    pantalla1.mostrarMensaje();
    pantalla2.mostrarMensaje();
    pantalla3.mostrarMensaje();
    delay(300);
    pantalla1.moverDerecha();
    pantalla2.moverIzquierda();
    pantalla3.moverDerecha();
  } else if (numeroArduino == 2) {
    pantalla1.mostrarMensaje();
    pantalla2.mostrarMensaje();
    // pausa en ms
    delay(700);
    pantalla1.moverDerecha();
    pantalla2.moverIzquierda();
  }
}