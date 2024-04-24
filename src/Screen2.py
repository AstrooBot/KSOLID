import pygame, sys
import Screen, Buttons
from Var_global import *


class Screen2(Screen.screen):
    
    def __init__(self):
        super().__init__()


class buttons2(Buttons.button):

    def __init__(self):
        self.screen = screen2.screen
        self.color = (255,255,0)
        self.width = 200
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_size = 35 
        self.text_color = (255,255,255)
        self.text_font_type = font_type


screen2 = Screen2()
screen2.display_init()

but_generate_map = buttons2()
but_generate_map.shape(screen_width*7/10,screen_height/4)
but_generate_map.set_text('Nuevo Mapa')

label_elements = screen2.font.render('Elementos', 1, font_color_title) 

but_add_element = buttons2()
but_add_element.text_size = 50
but_add_element.width = 40
but_add_element.height = 40
but_add_element.shape(screen_width/2,screen_height/4)
but_add_element.set_text('+')




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen2.set_title('Generacion de mapa')
    screen2.screen.blit(label_elements, (screen_width*7/10, screen_height*2/5))
    pygame.display.update()