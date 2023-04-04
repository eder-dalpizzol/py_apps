from flask import Flask, Response
import pygame

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((320, 240))

    # Draw a rectangle on the screen
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # Convert the screen surface to an image file
    image = pygame.image.tostring(screen, 'RGBA')

    # Return the image as a Flask response
    return Response(image, mimetype='image/png')
