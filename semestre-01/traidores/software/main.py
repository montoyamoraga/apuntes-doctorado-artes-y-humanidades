# importar modulos Python
import sys

# importar modulos externos
import pygame
import pygame.freetype

# importar modulos creados
from Administrador import Administrador
# import Promesa
# import Traicion

# definir constantes para colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
MAGENTA = (255, 0, 255)

# definir constantes para pygame
ANCHO = 800
ALTURA = 800
ALTURA_PANEL = 60
ALTURA_USABLE = ALTURA - ALTURA_PANEL
CUADROS_POR_SEGUNDO = 30

# iniciar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTURA))
reloj = pygame.time.Clock()


# constantes para los estados
ESTADO_INICIO = 'inicio'
ESTADO_NAVEGAR = 'navegar'
ESTADO_DOCUMENTAR = 'documentar'
ESTADO_AYUDA = 'ayuda'

# variable para estado
estado = ESTADO_INICIO

# instanciar administador
administrador = Administrador()

ft_font = pygame.freetype.SysFont('monospace', 20)

background = pygame.Surface(ventana.get_size())
pygame.draw.rect(background, NEGRO, background.get_rect())


def detectarTecla(event, estado):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            print('presionaste a')
            return ESTADO_AYUDA
        if event.key == pygame.K_i:
            print('presionaste i')
            return ESTADO_INICIO
        elif event.key == pygame.K_n:
            print('presionaste n')
            return ESTADO_NAVEGAR
        elif event.key == pygame.K_d:
            print('presionaste d')
            return ESTADO_DOCUMENTAR

    else:
        return estado


def mostrarTitulo(titulo):
    ft_font.render_to(
        ventana,
        (100, 100),
        titulo,
        BLANCO)


def mostrarSubTitulo(subtitulo):
    ft_font.render_to(
        ventana,
        (100, 200),
        subtitulo,
        BLANCO)


def mostrarTexto(texto, posY):
    ft_font.render_to(
        ventana,
        (100, posY),
        texto,
        BLANCO)


def mostrarAyuda():
    ventana.blit(background, (0, 0))
    mostrarTitulo('administrador de traiciones')
    mostrarSubTitulo(ESTADO_AYUDA)
    mostrarTexto('a: ayuda', 300)
    mostrarTexto('d: ayuda', 400)
    mostrarTexto('i: inicio', 500)
    mostrarTexto('n: ayuda', 600)


def mostrarDocumentar():
    ventana.blit(background, (0, 0))
    mostrarTitulo('administrador de traiciones')
    mostrarSubTitulo(ESTADO_DOCUMENTAR)


def mostrarInicio():
    ventana.blit(background, (0, 0))
    mostrarTitulo('administrador de traiciones')
    mostrarSubTitulo(ESTADO_INICIO)


def mostrarNavegar():
    ventana.blit(background, (0, 0))
    mostrarTitulo('administrador de traiciones')
    mostrarSubTitulo(ESTADO_NAVEGAR)


while True:
    reloj.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif estado == ESTADO_AYUDA:
            mostrarAyuda()
            estado = detectarTecla(event, estado)
        elif estado == ESTADO_DOCUMENTAR:
            mostrarDocumentar()
            estado = detectarTecla(event, estado)
        elif estado == ESTADO_INICIO:
            mostrarInicio()
            estado = detectarTecla(event, estado)
        elif estado == ESTADO_NAVEGAR:
            mostrarNavegar()
            estado = detectarTecla(event, estado)
        else:
            estado = detectarTecla(event, estado)
            print("whatever")

    # ft_font.render_to(ventana, (100, 150), 'traicion-01', BLANCO)

    # iterator = 0

    # for i in administrador.data['traiciones'][0]:
    #     iterator = iterator + 1
    #     # print(i, data['traiciones'][0][i])
    #     ft_font.render_to(ventana, (100, 200 + iterator*50), i, MAGENTA)
    #     ft_font.render_to(ventana,
    #                       (150, 220 + iterator*50),
    #                       administrador.data['traiciones'][0][i], VERDE)

    pygame.display.flip()
