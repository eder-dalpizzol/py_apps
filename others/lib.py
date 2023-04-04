import pygame, random
import numpy as np

def draw_lines(screen,x, y):
    """Draw the lines from the mouse position to each corner"""
    pygame.draw.line(screen, (255, 255, 255), (x, y), (0, 0))
    pygame.draw.line(screen, (255, 255, 255), (x, y), (0, 500))
    pygame.draw.line(screen, (255, 255, 255), (x, y), (700, 0))
    pygame.draw.line(screen, (255, 255, 255), (x, y), (700, 500))

def create_fireworks(screen, pos):
    particles = []
    for i in range(100):
        particle_x, particle_y = pos
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        velocity_x = random.uniform(-8, 8)
        velocity_y = random.uniform(-8, 8)
        particles.append((particle_x, particle_y, color, velocity_x, velocity_y))
    for i in range(100):
        for j in range(len(particles)):
            particle = particles[j]
            particle_x, particle_y, color, velocity_x, velocity_y = particle
            particle_x += velocity_x
            particle_y += velocity_y
            pygame.draw.circle(screen, color, (particle_x, particle_y), 2)
        pygame.display.flip()
        pygame.time.wait(10)

def create_box(screen, pos):
    # 3D box points
    points = [(pos[0]-20, pos[1]-20), (pos[0]+20, pos[1]-20), (pos[0]+20, pos[1]+20), (pos[0]-20, pos[1]+20)]

    # Rotate points
    angle = random.randint(0, 360)
    points = [pygame.math.Vector2(p).rotate(angle) for p in points]

    # Draw white outline of the box
    pygame.draw.lines(screen, (255, 255, 255), True, points, 2)
    pygame.display.flip()

def render_box(screen):
    width, height = screen.get_size()
    center_x, center_y = width//2, height//2
    angle = pygame.time.get_ticks() // 50
    theta = angle * np.pi / 180
    camera_distance = height//2
    fov = np.pi/3
    aspect = width/height
    #3D box points (diagonal view)
    diagonal_box = np.array([
        [-width//4, -height//4, -height//4],
        [width//4, -height//4, -height//4],
        [width//4, height//4, -height//4],
        [-width//4, height//4, -height//4],
        [-width//4, -height//4, height//4],
        [width//4, -height//4, height//4],
        [width//4, height//4, height//4],
        [-width//4, height//4, height//4],
    ])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    diagonal_box = diagonal_box @ R
    diagonal_box[:, 0] += center_x
    diagonal_box[:, 1] += center_y
    diagonal_box[:, 2] += camera_distance
    
    diagonal_box[:,0] = diagonal_box[:,0] * camera_distance/diagonal_box[:,2] * np.tan(fov/2) * aspect
    diagonal_box[:,1] = diagonal_box[:,1] * camera_distance/diagonal_box[:,2] * np.tan(fov/2)
    diagonal_box = diagonal_box[:, :2]
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.polygon(screen, (255, 255, 255), diagonal_box.tolist(), 2)

