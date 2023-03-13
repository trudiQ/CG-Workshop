import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600 
rotAngle = 0 # rotation angle around y-axis, incremental 
translateVec = [0.0, 0.0, 0.0] # translate along x, y, z

vertices = (
    (1, -1, -1),        #v0
    (1, 1, -1),         #v1
    (-1, 1, -1),        #v2
    (-1, -1, -1),       #v3
    (1, -1, 1),         #v4 
    (1, 1, 1),          #v5
    (-1, 1, 1),         #v6
    (-1, -1, 1)         #v7
)

edges = (
    (0, 1),             #e0: v0,v1
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 6),
    (7, 3),
    (7, 4),
    (7, 6),
    (5, 1),
    (5, 4),
    (5, 6)
)

faces = (
    (0, 1, 5, 4),       #f0: v0,v1,v5,v4
    (3, 2, 6, 7),
    (1, 2, 6, 5),
    (0, 3, 7, 4),
    (0, 1, 2, 3),
    (4, 5, 6, 7)
)

def Cube():
    glPushMatrix()
    # TODO: transform the cube


    # TODO: draw faces (quads)


    # TODO: draw edges (lines)

    
    # TODO: draw vertices


    glPopMatrix()
    pass

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(100.0, 0.0, 0.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 100.0, 0.0)                                             # v1
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

def draw():                                                     # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    
    # create a spinning cube
    Cube()

    # TODO: create a movable cube


def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('Hello Cube')                                # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100.0)                        # specify perspective projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 10, 0, 0, -1, 0, 1, 0)
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    global translateVec
    while True:
        bResetModelMatrix = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

            if event.type == pygame.KEYDOWN:
                # '0' reset the view
                if event.key == pygame.K_0:
                    bResetModelMatrix = True

                # TODO: keyboard controls "movableCube"    


        draw()
        drawAxes()
        
        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
            
        pygame.display.flip()
        pygame.time.wait(10)

main()