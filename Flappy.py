import pygame
from pygame.locals import *
import sys

pygame.init()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (250,0,0)



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

    def collision(self,can):

        #if self.x + self.width == can.x:
            #if self.y <= can.y - can.height or self.y >= can.y:
                #print("pegou right ")
               # sys.exit()

        if self.x + self.height >= can.x and self.x <=  can.x + can.width:

            if self.y <= can.y - can.height or self.y >= can.y:
                sys.exit()

            elif self.y + self.height >=can.y:
                sys.exit()

        if self.y  >=  SCREEN_HEIGHT or self.y + self.height < 0:
            sys.exit()









class Cano:

    def __init__(self, x,y, height, width, color, display):

        self.color =  color
        self.display = display
        self.x =  x
        self.y =  y
        self.height = height
        self.width = width

    def Draw_Cano(self, direction):

        self.direction = direction

        if self.direction == "top":
            self.y = 0

        else:
            self.y = 400

        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])



    def Run_Cano(self, speed):

        self.speed =  speed

        self.x =  self.x - speed



bird = Bird(100, 250, 30, 30, WHITE, screen)
plataforma = Cano(400, 400, 200, 30, WHITE, screen)





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                bird.Jump()


    if plataforma.x + plataforma.width < 0:
        plataforma = Cano(400, 400, 200, 30, WHITE, screen)



    print(bird.y)


    bird.collision(plataforma)


    screen.fill(BLACK)
    bird.Draw_Bird()
    bird.Fall()
    plataforma.Draw_Cano("top")
    plataforma.Draw_Cano("bottom")
    plataforma.Run_Cano(0.04)
    pygame.display.update()
