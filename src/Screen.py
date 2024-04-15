
import pygame, Var_global


pygame.init()
class screen() :

    
    def __init__(self):
        self.size = self.width, self.height = Var_global.screen_width, Var_global.screen_height
        self.caption = "KSOLID Game"
        self._image = None
        self.background_image = None
        self.background_image_rect = None
        self.screen = None
        self.font = pygame.font.Font(Var_global.font_type, Var_global.font_size_title)

    
    def set_caption(self):
        pygame.display.set_caption(self.caption)

  
    def set_background_image(self):
        self.background_image = pygame.image.load(self._image).convert()
        self.background_image_rect = self.background_image.get_rect()
        

    def get_background_image(self):
        return self.background_image
    

   
    def display_screen(self):
        self.screen = pygame.display.set_mode(self.size)
    

    
    def get_display_screen(self):
        return self.screen
    

    
    def display_init(self):
        pygame.init()
        self.set_caption()
        self.display_screen()


    def set_title(self,text):
    
        title = self.font.render(text, 1, Var_global.font_color_title) 
        self.screen.blit(title,(Var_global.screen_width/3, Var_global.screen_height/8))   
    
    





"""class Screen1(Iscreen):

    def __init__(self):
        super().__init__()
        self._image = "./src/tabladistros.jpeg"

pygame.init()
lol = Screen1()
lol.set_title()
lol.display_screen()
lol.set_background_image()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    lol.screen.blit(lol.background_image,lol.background_image_rect)
    pygame.display.update()"""

