import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Set the position of the square on the screen
square_x = 400
square_y = 300

# Set the size of the square
square_size = 50

speed = 0.5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the keys that are being pressed
    keys = pygame.key.get_pressed()

    # Move the square based on the keys being pressed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        square_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        square_y += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        square_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        square_x += speed

    # Draw a random color square on the screen
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, random_color, (square_x, square_y, square_size, square_size))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
