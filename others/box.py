from OpenGL.GLU import *
from OpenGL.GLUT import *

def create_box():
    angle = pygame.time.get_ticks() // 50
    glMatrixMode(GL_MODELVIEW)
    glRotatef(angle, 1, 1, 1)
    glutSolidCube(1)
