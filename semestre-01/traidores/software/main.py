# importar modulos
import pygame
import pygame.freetype

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

ft_font = pygame.freetype.SysFont('monospace', 30)

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

    ft_font.render_to(window, (100, 200), 'traicion-01', WHITE)

    
    pygame.display.flip()

pygame.quit()
exit()