import pygame
import random
from pygame.locals import *
from random import randint



#Definir algunos parámetros de formulario y cargar archivos de fuentes
SCREEN_WIDTH  = 900         # Ancho de ventana
SCREEN_HEIGHT = 600         # Ancho de ventana
LOW_SPEED  = 4              # Velocidad mínima de movimiento de la fuente
HIGH_SPEED = 10             # Movimiento de fuente más rápido
FONT_COLOR = (00,150,00)    # color de fuente
FONT_SIZE = 5               # Tamaño de fuente
FONT_NOM  = 20              # Mostrar el número de fuente a partir de 0
FONT_NAME = 1  # Tenga en cuenta que el nombre del archivo de la fuente debe ser exactamente el mismo que el archivo real (tenga en cuenta el caso de ttf), y el nombre del archivo no puede ser chino
FREQUENCE = 10              # Frecuencia de tiempo
times = 0                   # Tiempo de inicialización


# Definir parámetros aleatorios
def randomspeed() :
    return randint(LOW_SPEED,HIGH_SPEED)
def randomposition() :
    return randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT)
def randomoname() :
    return randint(0,100000)
def randomvalue() :
    return randint(0,100)              # this is your own display number range


#class of sprite
class Word(pygame.sprite.Sprite) :
    def __init__(self,bornposition) :
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        self.image = self.font.render(str(self.value),True,FONT_COLOR)
        self.speed = randomspeed()
        self.rect = self.image.get_rect()
        self.rect.topleft = bornposition

    def update(self) :
        self.rect = self.rect.move(0,self.speed)
        if self.rect.top > SCREEN_HEIGHT :
            self.kill()


#init the available modules
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ViatorSun CodeRain")
clock = pygame.time.Clock()
group = pygame.sprite.Group()
group_count = int(SCREEN_WIDTH / FONT_NOM)


#mainloop
while True :
    time = clock.tick(FREQUENCE)
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    for i in range(0,group_count) :
        group.add(Word((i * FONT_NOM,-FONT_NOM)))

    group.update()
    group.draw(screen)
    pygame.display.update()