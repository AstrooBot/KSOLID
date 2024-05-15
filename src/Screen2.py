import pygame, Buttons, Var_global , Iscreen

class screen2(Iscreen.screen): 
    def __init__(self,screen):
        super().__init__(screen)

    def display(self, event_list):

        but_generate_map = buttons2(self.screen)
        but_generate_map.shape(Var_global.screen_width*7/10,Var_global.screen_height/4)
        but_generate_map.set_text('Nuevo Mapa')
        label_elements = self.font.render('Elementos', 1, Var_global.font_color_title) 
        but_add_element = buttons2(self.screen)
        but_add_element.text_size = 50
        but_add_element.width = 20
        but_add_element.height = 20
        but_add_element.shape(Var_global.screen_width/2,Var_global.screen_height/4)
        but_add_element.set_text('+')
        self.set_title('Generacion de mapa')
        self.screen.blit(label_elements, (Var_global.screen_width*7/10, Var_global.screen_height*2/5))

class buttons2(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = (255,255,0)
        self.width = 200
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_size = 35 
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
          