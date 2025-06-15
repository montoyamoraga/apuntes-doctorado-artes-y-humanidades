# importar modulos
import pygame
import pygame.freetype
import pygwidgets
import json

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)

data = None

# abrir el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ft_font = pygame.freetype.SysFont('monospace', 20)

background = pygame.Surface(window.get_size())
pygame.draw.rect(background, BLACK, background.get_rect())

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))

    ft_font.render_to(window, (100, 100), 'administrador de traiciones', WHITE)

    ft_font.render_to(window, (100, 150), 'traicion-01', WHITE)

    # print(data['traiciones'][0])
    iterator = 0

    for i in data['traiciones'][0]:
        iterator = iterator + 1
        # print(i, data['traiciones'][0][i])
        ft_font.render_to(window, (100, 200 + iterator*50), i, MAGENTA)
        ft_font.render_to(window, (150, 220 + iterator*50), data['traiciones'][0][i], GREEN)

    pygame.display.flip()

pygame.quit()
exit()
