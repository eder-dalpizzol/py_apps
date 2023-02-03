import pygame
import random

# initialize pygame
pygame.init()

# set display size
screen = pygame.display.set_mode((500, 500))

# set player size and position
player_size = 50
player_pos = [50, 400]

# set speed
speed = 0.1

# set jump speed and height
jump_speed = -5
jump_height = 50

# set floor color and position
floor_color = (0, 255, 0)
floor_pos = [0, 450, 500, 50]

# game loop
running = True
jumping = False
jump_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
    
    # update player position
    player_pos[0] += speed
    
    # handle jump
    if jumping:
        if jump_count >= -jump_height:
            player_pos[1] += (jump_count * abs(jump_count)) / 2 * jump_speed
            jump_count += jump_speed
        else:
            jump_count = 0
            jumping = False
            player_pos[1] = 400
    
    # fill screen with white
    screen.fill((255, 255, 255))
    
    # draw floor
    pygame.draw.rect(screen, floor_color, floor_pos)
    
    # draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))
    
    # update display
    pygame.display.update()

# quit pygame
pygame.quit()
