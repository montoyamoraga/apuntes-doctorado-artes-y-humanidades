# clase-10

martes 28 octubre 2025

## tarea 1: introducción artículo académico

estrategias de secuencias de sampleos de material sonoro hablado

el habla humana es una secuencia de sonidos. con herramientas computacionales se pueden transcribir esos sonidos a texto, no solamente la palabra, también su tiempo de aparición y desaparición, su duración, pausas, entonación, y trayectorias de frecuencias.

al transcribir el habla a texto y material, se pueden disponer en distintas estrategias de secuencias. en este texto mostraremos distintas estrategias para secuenciar material sonoro, con énfasis en secuenciadores de hardware electrónicos, y proponemos nuevas formas de secuenciar material sonoro hablado.

## tarea 2: texto escrito con citas

explicación: con las herramientas videogrep y vosk transcribí tres discursos de allende, y le pedí que me dijera las frases de 3 palabras más repetidas de cada uno, luego seleccioné las 10 más repetidas de cada uno.

1972-12-02

de los países 8
la inmensa mayoría 6
la universidad de 5
universidad de guadalajara 5
de mi patria 5
en mi patria 5
la asignación familiar 5
que la juventud 5
a través de 4
de américa latina 4

1972-12-04

millones de dólares 17
de las naciones 15
las naciones unidas 15
de los países 15
mil novecientos setenta 10
mil millones de 8
en mil novecientos 8
los países del 8
del tercer mundo 7
los países en 7

1973-11-09

tengo la certeza 3
trabajadores de mi 2
de mi patria 2
ha dirigido vuelve 1
dirigido vuelve a 1
vuelve a la 1
a la torre 1
la torre portales 1
torre portales y 1
portales y radio 1

con estos comandos tomé las 10 frases de cada discurso, y generé los audios correspondientes adjuntos en este repositorio.

```bash
videogrep --input audios-procesados/1972-12-02.wav --search "de los países" --search "la inmensa mayoría" --search "la universidad de" --search "universidad de guadalajara" --search "de mi patria" --search "en mi patria" --search "la asignación familiar" --search "que la juventud" --search "a través de" --search "de américa latina" --search-type "fragment" --output  1972-12-02.wav
```

```bash
videogrep --input audios-procesados/1972-12-04.wav --search "millones de dólares" --search "de las naciones" --search "las naciones unidas" --search "de los países" --search "mil novecientos setenta" --search "mil millones de"  --search "en mil novecientos" --search "los países del" --search "del tercer mundo" --search "los países en"  --search-type "fragment" --output  1972-12-04.wav
```

```bash
videogrep --input audios-procesados/1973-09-11.wav --search "tengo la certeza" --search "trabajadores de mi" --search "de mi patria" --search "ha dirigido vuelve" --search "dirigido vuelve a" --search "vuelve a la" --search "a la torre" --search "la torre portales" --search "torre portales y" --search "portales y radio" --search-type "fragment" --output  1973-09-11.wav
```

## lectura 1: Cajas (Montalbetti)

precioso texto.

me recuerda mucho a la matemática en el libro purgatorio de raúl zurita

las promesas se usan en JavaScript para manejar asincronía.

la topología de lo que es 2D y 3D me emociona.

para describir un objeto, es importante describir los ejes, su taxonomía.

## lectura 2: Manifiesto decimista

el texto entero está escritos en décimas.

pasó un año entre submitted y accepted.

tiene muchas citas explicativas.

fue publicado bajo licencia creative commons.

fue publicado en la revista trans - revista transcultural de música

<https://www.sibetrans.com/trans>
