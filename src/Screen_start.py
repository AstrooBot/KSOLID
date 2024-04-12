"""Objective: dev the differents screens"""
import pygame, sys
import Buttons
from Var_global import *


pygame.init()

screen_start = pygame.display.set_mode(screen_size)

font = pygame.font.Font(font_type, 58)
text = font.render('Bienvenido a KSOLID', 1, (255,255,255))

but_start = Buttons.button(screen_start, (255,0,255), 100, 50)
but_start.shape(screen_width/2-but_start.width,screen_height/2-but_start.height)





def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen_start.blit(text, (screen_width/3.22, screen_height/8.22r))
        pygame.display.update()
        

if __name__ == "__main__":
    main()
    
    
