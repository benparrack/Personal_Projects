import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Debugging")

# Set up the perspective
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Set the clear color to a light gray for visibility
glClearColor(0.5, 0.5, 0.5, 1.0)

# Cube vertices and edges
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Game loop flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Apply a static camera transformation
    glTranslatef(0.0, 0.0, -5)

    # Draw the cube
    draw_cube()

    # Debugging: Print OpenGL errors
    error = glGetError()
    if error != GL_NO_ERROR:
        print(f"OpenGL Error: {error}")

    # Update display
    pygame.display.flip()
    pygame.time.wait(10)

# Quit pygame
pygame.quit()