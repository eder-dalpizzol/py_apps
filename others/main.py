import pygame
from lib import draw_lines, render_box

# Initialize pygame
pygame.init()

# Set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Mouse Position")

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            x, y = pos
            draw_lines(screen,x, y)
    
    render_box(screen)
    pygame.display.flip()

# Exit pygame
pygame.quit()
