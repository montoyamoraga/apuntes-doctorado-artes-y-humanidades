# curso traduccion intersemiotica
# dictado por profesora doctora jèssica pujol
# tarea por aaron montoya
# lunes 17 noviembre 2025

import random
import os


alfabeto = "abcdefghijklmnopqrstuvwxyzñ"


# crear una silaba aleatoria entre 1 y 3 caracteres
def silabaAleatoria():
    largo = random.randint(1, 3)
    return ''.join(random.choice(alfabeto) for x in range(largo))


# funcion que usa comando say de macOS
# para leer texto en cierta voz y cierta velocidad
def glossolalia(text, voice="Francisca", velocidad=200):
    command = f'say -v {voice} -r {velocidad} "{text}"'
    os.system(command)


while True:
    silabas = [silabaAleatoria() for x in range(10)]
    texto = ''.join(silabas)
    print(texto)
    velocidad = random.randint(150, 300)
    glossolalia(texto, "Francisca", velocidad)

