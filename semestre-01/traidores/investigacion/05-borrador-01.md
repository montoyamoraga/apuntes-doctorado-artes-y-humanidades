# borrador-01

administración de la traición con computadores

## definición de traición computacional

traición electrónica implica agencia de la electrónica. en la electrónica podemos cometer errores, podemos también tener promesas incumplidas, como un cable que nos promete hacer una conexión eléctrica, pero que está roto por dentro y no lo sabemos. Pero no existe la voluntad del dispositivo o material de traicionarnos, no toma la decisión de romper nuestra confianza, por lo que no califica como traición.

traición computacional enfrenta el mismo paradigma, el computador trata de cumplir nuestras promesas, pero no siempre lo logra, ya que comete errores, pierde alimentación, o porque creímos haber depositado nuestra confianza en instrucciones claras, pero no lo eran.

definición de traición con bibliografía y su manejo en electrónica y computación

## manejo de traición a nivel computacional

ontología orientada a objetos

los computadores son herramientas que pueden almacenar y procesar datos.

la traición la podemos definir como una estructura de datos, con un conjunto de operaciones para hacer transiciones de estado.

## estado del arte de computadores personales de uso específico

Uso de microcontroladores Arduino para diseñar dispositivos computacionales.

Uso de computadores Raspberry Pi para obras de arte electrónico.

## investigación de software para administrar traición

softwares para administrar confianza.

softwares de uso sensible para periodistas: Proyecto Guardian <https://guardianproject.info/>.

Protocolo de encriptamiento <https://signal.org/>

La promesa del software SecureDrop es Share and accept documents securely. <https://securedrop.org/>

Traición por parte de SourceForge: [<https://www.theregister.com/2013/12/20/sourceforge_betrayal/>.](https://arstechnica.com/information-technology/2015/06/sourceforge-locked-in-projects-of-fleeing-users-cashed-in-on-malvertising/)

## investigación de hardware para administrar traición

The Claw of Shame in Nathan Fielder <https://www.imdb.com/title/tt2780878/>

## diseño, desarrollo y construcción de aparato computacional administrador de traiciones

durante esta investigación diseñé clases para definir traicion y otras clases asociadas, con los siguientes atributos y métodos:

atributos:

- nombre
- fecha de creación
- fecha de modificación
- estado (confianzaDepositada, confianzaRetirada, traicion)
- receptor
- emisor
- descripción

metodos:

- depositarConfianza()
- retirarConfianza()
- traicionar()

como inspiración usamos los dispositivos computacionales de monome, como norns, y los de Critter and Guitari, como Organelle y Eyesy.

Se propone este administrador de traiciones como un dispositivo que permite a los usuarios registrar y administrar sus traiciones, tanto las recibidas como las emitidas.

Para la visualización se proponen varios métodos:

el primer prototipo ocurre en una interfaz hecha en Python, con la biblioteca pygame.

el siguiente prototipo es un aparato standalone, con una pantalla LCD y botones y teclado para navegar las traiciones.

Para hardware proponemos un microcontrolador Raspberry Pi Pico 2, basado en el microcontrolador RP2050, de bajo costo y bajo consumo.

Como salida, proponemos una pantalla LCD de 128x64 pixeles, para mostrar texto.

## conclusiones y pasos a seguir sobre el aparato construido

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
