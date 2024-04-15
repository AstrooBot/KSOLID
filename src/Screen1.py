
import pygame, sys
import Iscreen, Buttons
from Var_global import *


class Screen1(Iscreen.Iscreen):
    
    def __init__(self):
        super().__init__()


class buttons1(Buttons.button):

    def __init__(self):
        self.screen = screen1.screen
        self.color = button_color
        self.width = 170
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
       


pygame.init()
screen1 = Screen1()
screen1.set_title()
screen1.display_screen()

font = pygame.font.Font(font_type, 58)

text = font.render('Bienvenido a KSOLID', 1, (255,255,255))
but_start = buttons1()
but_start.shape(screen_width/2-but_start.width/2,screen_height/2-but_start.height/2)
but_start.set_text('Jugar',(255,255,255), 35, font_type)

but_es = buttons1()
but_es.shape(screen_width/2-but_start.width/2, screen_height*3/4-but_es.height/2)
but_es.set_text('Como jugar',(255,255,255), 35, font_type)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen1.screen.blit(text, (screen_width/3, screen_height/8))
    
    pygame.display.update()








""""font = pygame.font.Font(font_type, 58)
text = font.render('Bienvenido a KSOLID', 1, (255,255,255))

but_start = Buttons.button(screen_start, (255,0,255), 100, 50)
but_start.shape(screen_width/3+but_start.width,screen_height/2-but_start.height)





def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen_start.blit(text, (screen_width/3, screen_height/8))
        pygame.display.update()
        

if __name__ == "__main__":
    main()
    
    """
