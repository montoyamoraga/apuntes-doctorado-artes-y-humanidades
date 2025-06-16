# borrador-02

administración de la traición con computadores

## definición de traición computacional

La traición electrónica implica agencia de la electrónica.

En la electrónica podemos cometer errores, podemos también tener promesas incumplidas, como un cable que nos promete hacer una conexión eléctrica, pero que está roto por dentro y no lo sabemos. Pero no existe la voluntad del dispositivo o material de traicionarnos, no toma la decisión de romper nuestra confianza, por lo que no califica como traición.

La traición computacional enfrenta el mismo paradigma, el computador trata de cumplir nuestras promesas, pero no siempre lo logra, ya que comete errores, pierde alimentación, o porque creímos haber depositado nuestra confianza en instrucciones claras, pero no lo eran.

definición de traición con bibliografía y su manejo en electrónica y computación

## manejo de traición a nivel computacional

ontología orientada a objetos

los computadores son herramientas que pueden almacenar y procesar datos.

la traición la podemos definir como una estructura de datos, con un conjunto de operaciones para hacer transiciones de estado.

## estado del arte de computadores personales de uso específico

A principios del siglo XX la educación computacional para crear herramientas para artistas y diseñadores era muy limitada, centrándose principalmente en el uso de herramientas de software construidas por la industria.

Gracias al trabajo de Casey Reas y Ben Fry, con su herramienta Processing, creada al alero del laboratorio aesthetics and computation de MIT Media Lab, se logró popularizar el uso de software, para que artistas pudieran crear sus propias herramientas computacionales, bajo el paradigma de este framework de programación en Java.

De hecho Casey Reas fue uno de los co-advisors de la tesis de magíster de Hernando Barragán, quien creó el lenguaje de programación Wiring, que luego tras una traición de otro profesor conformó el proyecto Arduino, que popularizó el uso de microcontroladores para crear máquinas electrónicas.

Revisar el trabajo de Hernando Barragán, <https://arduinohistory.github.io/>

Hoy en día el flujo de artistas creando máquinas para sus obras tienen varios caminos posibles:

1. Correr código desde un computador de escritorio o laptop, con sistema operativo GNU/Linux, macOS o Windows.
1. Correr código en un computador de uso personal dedicado a instalaciones u obra, como una Raspberry Pi, o un Raspberry Pi Computer Module.
  1.1. Ejemplos: computador Norns de monome.
1. Programar un microcontrolador, Arduino o similar, donde el código corra directamente, sin necesidad de un computador más potente.

## investigación de software relacionado a la traición

La revisión bibliográfico de softwares que contenga la palabra traición no ha dado resultados.

softwares para administrar confianza.

softwares de uso sensible para periodistas: Proyecto Guardian <https://guardianproject.info/>.

Protocolo de encriptamiento <https://signal.org/>

La promesa del software SecureDrop es Share and accept documents securely. <https://securedrop.org/>

Traición por parte de SourceForge: [<https://www.theregister.com/2013/12/20/sourceforge_betrayal/>.](https://arstechnica.com/information-technology/2015/06/sourceforge-locked-in-projects-of-fleeing-users-cashed-in-on-malvertising/)

## investigación de hardware relacionado a la traición

A nivel de traición con hardware, queremos destacar el trabajo del comediante Nathan Fielder, quien en su programa de televisión "Nathan for You" comisión la creación de un dispositivo llamado The Claw of Shame <https://www.imdb.com/title/tt2780878/>.

Este dispositivo es una garra mecánica capaz de bajarle sus pantalones en público. Su contexto de uso es probar al usuario si es capaz de hacer una destreza y desactivar el dispositivo contra reloj, ya que si el dispositivo se activa, el usuario queda expuesto a la vergüenza pública y las repercusiones legales de estar sin pantaleones en público.

## diseño y desarrollo de software administrador de traiciones

Debido a su flexibilidad de uso y legibilidad, se decidió usar el software Python para el primer prototipo de administrar traiciones.

Luego se propone el porte a C++ para que pueda correr un microcontrolador Raspberry Pi Pico 2.

durante esta investigación diseñé clases para definir traicion y otras clases asociadas, con los siguientes atributos y métodos:

atributos:

* nombre
* fecha de creación
* fecha de modificación
* estado (confianzaDepositada, confianzaRetirada, traicion)
* receptor
* emisor
* descripción

metodos:

* depositarConfianza()
* retirarConfianza()
* traicionar()

como inspiración usamos los dispositivos computacionales de monome, como norns, y los de Critter and Guitari, como Organelle y Eyesy.

Se propone este administrador de traiciones como un dispositivo que permite a los usuarios registrar y administrar sus traiciones, tanto las recibidas como las emitidas.

Para la visualización se proponen varios métodos:

el primer prototipo ocurre en una interfaz hecha en Python, con la biblioteca pygame.

el siguiente prototipo es un aparato standalone, con una pantalla LCD y botones y teclado para navegar las traiciones.

Para hardware proponemos un microcontrolador Raspberry Pi Pico 2, basado en el microcontrolador RP2050, de bajo costo y bajo consumo.

Como salida, proponemos una pantalla LCD de 128x64 pixeles, para mostrar texto.

## conclusiones y pasos a seguir sobre el aparato construido

La primera aproximación de este software fue la investigación de.

Luego

Esta estructura de datos y sus operaciones puede ahora ser testeada y mejorada según feedback de los usuarios.

se propone construir una primera versión de los dispositivos físicos.

## bibliografía

<https://nostarch.com/art-arm-assembly-volume-1>

No Starch Press

Python

C++

Raspberry Pi

Lauren Lee McCarthy

Sam Lavigne y Tega Brain

Sasha Costanza-Chock
