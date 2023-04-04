import pygame
import random
from lib import create_fireworks, create_box

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (700, 500)
screen = pygame.display.set_mode(size)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                create_fireworks(screen,pos)
            elif event.button == 3:
                create_box(screen, pos)
    
    pygame.display.flip()

# Exit Pygame
pygame.quit()
