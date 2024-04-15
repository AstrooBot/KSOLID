import pygame, sys
import Screen, Buttons
from Var_global import *


class Screen1A(Screen.screen):
    
    def __init__(self):
        super().__init__()


class buttons1A(Buttons.button):

    def __init__(self):
        self.screen = screen1A.screen
        self.color = (255,255,255)
        self.width = 50
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)

screen1A = Screen1A()
screen1A.display_init()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    pygame.display.update()