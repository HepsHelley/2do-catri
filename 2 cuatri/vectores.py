import pygame
from pygame.locals import *
from math import *
escala = 30

class Vector:
    def __init__(self, color,dimenciones, origen):
        self.color = color
        self.origin = origen
        self.dimensions = dimenciones

    def calculo(self):
            x1, y1 = self.origen
            x2, y2 = self.dimenciones
            self.end = x1 + (x2 * escala), y1 - (y2 * escala)




pygame.init()
 
pygame.display.set_mode((640,480))
 
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()