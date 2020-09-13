import pygame
from pygame.locals import *
import random
import sys

pygame.init()


WHITE = (255,255,255)
BLACK = (0,0,0)


SCREEN_WIDTH = 400
SCREEN_HEIGHT =  600

screen =  pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


class Bird:

    def __init__(self, x,y, height, width, color, display):
        self.x = x
        self.y = y
        self.height =  height
        self.width = width
        self.color = color
        self.display =  display

    def Draw_Bird(self):
        pygame.draw.rect(self.display,self.color,[self.x, self.y, self.width, self.height])

    def Jump(self):
        self.y = self.y + -30

    def Fall(self):

        self.y = self.y  + 0.05

 #AABB logic

    def collision(self, can):

        birdRight = self.x + self.width
        birdBottom = self.y + self.height
        canRight = can.x + can.larg
        canBottom = can.y + can.alt
        if birdBottom < can.y or self.y > canBottom or birdRight < can.x or self.x > canRight:
            pass
        else:
            sys.exit()



class Cano:

    def __init__(self, y, alt, x):

        self.alt =  alt
        self.y = y
        self.larg = 30
        self.x = x
        self.vHor = 0.05

    def draw(self):

        pygame.draw.rect(screen, WHITE, [self.x, self.y, self.larg, self.alt])

    def run(self):

        self.x -=  self.vHor





def Generate(lista):

    a =  random.randint(100,300)
    lista.append(Cano( 0, a, 400))
    lista.append(Cano( a +150, SCREEN_HEIGHT - (a + 150),400))



array = []
Generate(array)


bird = Bird(100, 250, 30, 30, WHITE, screen)





while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                bird.Jump()


    screen.fill(BLACK)

    bird.Fall()


    for i in array:
        bird.Draw_Bird()
        i.draw()
        i.run()
        bird.collision(i)
        if array[len(array)-1].x < 200:
            Generate(array)
       

        if len(array) > 8:
            array.pop(0)
            array.pop(1)


    pygame.display.update()
