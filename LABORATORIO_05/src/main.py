import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Primer Juego con Pygame")

# Color de fondo
background_color = (0, 0, 0)  # Negro

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellena la pantalla con el color de fondo
    screen.fill(background_color)

    # Actualiza la pantalla
    pygame.display.flip()
