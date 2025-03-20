// simulador de pantalla de norns
// por montoyamoraga
// marzo 2025
// processing 4.3.4

// dimensiones originales de norns
int ancho = 128;
int alto = 64;

// multiplicador de tamano de pixeles
int multiplicador = 1;

// niveles de brillos
int brillosNiveles = 16;

// brillos minimo y maximo
int brilloMin = 0;
int brilloMax = 255;

int[] brillos;


void settings() {
  multiplicador = 8;
  size(ancho * multiplicador,
    alto * multiplicador);
}

void setup() {
  background(0);
  inicializarBrillos();
  probarBrillos();
}

void draw() {
}

void inicializarBrillos() {
  // crear array de brillos
  brillos = new int[brillosNiveles];

  // recorrer todos los brillos
  for (int i = 0; i < brillosNiveles; i++) {
    brillos[i] = brilloMin +
      i*(brilloMax - brilloMin)/brillosNiveles;
    // println(brillos[i]);
  }
}

void probarBrillos() {

  noStroke();
  rectMode(CORNER);

  int indiceBrillo = floor(random(0, brillosNiveles));

  for (int y = 0; y < height; y = y + multiplicador * pixelDensity) {
    for (int x = 0; x < width; x = x + multiplicador * pixelDensity) {

      fill(color(brillos[indiceBrillo]));

      // color brilloAleatorio = color(brillos[floor(random(0, brillosNiveles))]);
      // fill(brilloAleatorio);

      rect(x, y, multiplicador, multiplicador);

      indiceBrillo = indiceBrillo + floor(random(0, 2));

      indiceBrillo = indiceBrillo % brillosNiveles;

      //if (indiceBrillo < 0) {
      //  indiceBrillo = 0;
      //}

      //if (indiceBrillo > brillosNiveles - 1) {
      //  indiceBrillo = brillosNiveles - 1;
      //}
    }
  }


  // loadPixels();
  //for (int i = 0; i < width * height * pixelDensity; i = i + multiplicador) {
  //  color brilloAleatorio = color(brillos[floor(random(0, brillosNiveles))]);
  //  for (int x = 0; x < multiplicador; x++) {
  //    for (int y = 0; y < multiplicador; y++) {
  //      pixels[i + x + y * multiplicador] = brilloAleatorio;
  //    }
  //  }
  //  updatePixels();
  //}
}

void mousePressed() {
  saveFrame("001.jpg");
}
