# importar modulos Python
import json
import sys
import os

# importar modulos externos
import pygame
import pygame.freetype

# importar modulos creados
from constantes import ANCHO, ALTURA
from constantes import BLANCO, CYAN, MAGENTA, NEGRO, VERDE
from constantes import ESTADO_AYUDA, ESTADO_DOCUMENTAR
from constantes import ESTADO_INICIO, ESTADO_NAVEGAR
from constantes import TITULO


class Administrador():

    def __init__(self):
        self.name = "administrador"
        self.traicionActiva = 0
        self.estado = ESTADO_INICIO
        self.traiciones = []
        # iniciar pygame
        pygame.init()
        pygame.display.set_caption(TITULO)
        self.ventana = pygame.display.set_mode((ANCHO, ALTURA))
        self.reloj = pygame.time.Clock()
        self.ft_font = pygame.freetype.SysFont('monospace', 20)
        self.background = pygame.Surface(self.ventana.get_size())
        pygame.draw.rect(self.background, NEGRO, self.background.get_rect())
        # abrir el archivo JSON
        cwd = os.path.dirname(os.path.abspath(__file__))
        archivo = cwd + '/data.json'
        with open(archivo, 'r') as file:
            self.data = json.load(file)
            self.parseJSON()

    def parseJSON(self):
        for i in self.data['traiciones']:
            self.traiciones.append(i)

    def detectarTecla(self, event, estado):
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
            elif event.key == pygame.K_LEFT:
                self.traicionActiva = self.traicionActiva - 1
                if self.traicionActiva < 0:
                    self.traicionActiva = 0
                return estado
            elif event.key == pygame.K_RIGHT:
                self.traicionActiva = self.traicionActiva + 1
                if self.traicionActiva >= len(self.traiciones):
                    self.traicionActiva = len(self.traiciones) - 1
                return estado
        else:
            return estado

    def mostrarTitulo(self, titulo):
        self.ft_font.render_to(
            self.ventana,
            (100, 100),
            titulo,
            BLANCO)

    def mostrarSubTitulo(self, subtitulo):
        self.ft_font.render_to(
            self.ventana,
            (100, 200),
            subtitulo,
            CYAN)

    def mostrarTexto(self, texto, posY):
        self.ft_font.render_to(
            self.ventana,
            (100, posY),
            texto,
            VERDE)

    def mostrarCampoNombre(self, texto, posY):
        self.ft_font.render_to(
            self.ventana,
            (100, posY),
            texto,
            VERDE)

    def mostrarCampoValor(self, i, posY):
        self.ft_font.render_to(
            self.ventana,
            (400, posY),
            self.traiciones[self.traicionActiva][i],
            MAGENTA)

    def mostrarCampoNombreValor(self, i, posY):
        self.mostrarCampoNombre(i, posY)
        self.mostrarCampoValor(i, posY)

    def mostrarAyuda(self):
        self.ventana.blit(self.background, (0, 0))
        self.mostrarTitulo(TITULO)
        self.mostrarSubTitulo(ESTADO_AYUDA)
        self.mostrarTexto('a: ayuda', 300)
        self.mostrarTexto('d: documentar', 400)
        self.mostrarTexto('i: inicio', 500)
        self.mostrarTexto('n: navegar', 600)

    def mostrarDocumentar(self):
        self.ventana.blit(self.background, (0, 0))
        self.mostrarTitulo(TITULO)
        self.mostrarSubTitulo(ESTADO_DOCUMENTAR)

    def mostrarInicio(self):
        self.ventana.blit(self.background, (0, 0))
        self.mostrarTitulo(TITULO)
        self.mostrarSubTitulo(ESTADO_INICIO)
        self.mostrarTexto('v0.0.1 junio 2025', 300)
        self.mostrarTexto('por montoyamoraga', 400)
        self.mostrarTexto(
            'para el curso traidores del profesor josé santos', 500)
        self.mostrarTexto('en el doctorado de artes y humanidades', 600)
        self.mostrarTexto('en idea usach', 700)

    def mostrarNavegar(self):
        self.ventana.blit(self.background, (0, 0))
        self.mostrarTitulo(TITULO)
        self.mostrarSubTitulo(ESTADO_NAVEGAR)
        iterador = 0
        for i in self.traiciones[self.traicionActiva]:
            iterador = iterador + 1
            self.mostrarCampoNombreValor(i, 300 + iterador * 50)

    def correr(self):
        self.reloj.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif self.estado == ESTADO_AYUDA:
                self.mostrarAyuda()
                self.estado = self.detectarTecla(event, self.estado)
            elif self.estado == ESTADO_DOCUMENTAR:
                self.mostrarDocumentar()
                self.estado = self.detectarTecla(event, self.estado)
            elif self.estado == ESTADO_INICIO:
                self.mostrarInicio()
                self.estado = self.detectarTecla(event, self.estado)
            elif self.estado == ESTADO_NAVEGAR:
                self.mostrarNavegar()
                self.estado = self.detectarTecla(event, self.estado)
            else:
                self.estado = self.detectarTecla(event, self.estado)
                # print("whatever")

        pygame.display.flip()
