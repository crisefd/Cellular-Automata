from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


class Window():

    def __display_lattice(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glColor3f(0.0, 1.0, 1.0)
        glVertex2f(-0.99, 0.98)
        glEnd()
        glFlush()

    def __init__(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(0, 0)
        glutCreateWindow('Cellular Automata')
        glLoadIdentity()
        glutDisplayFunc(self.__display_lattice)
        glutIdleFunc(self.__display_lattice)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glutMainLoop()


Window()
