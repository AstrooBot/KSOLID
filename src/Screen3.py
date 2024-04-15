import pygame, sys
import Screen, Buttons
from Var_global import *


class Screen3(Screen.screen):
    
    def __init__(self):
        super().__init__()


class buttons3(Buttons.button):

    def __init__(self):
        self.screen = screen3.screen
        self.color = (255,255,255)
        self.width = 50
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)

screen3 = Screen3()
screen3.display_init()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    pygame.display.update()