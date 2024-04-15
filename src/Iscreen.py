from abc import ABC, abstractmethod
import pygame, Var_global



class Iscreen(ABC) :

    @abstractmethod
    def __init__(self):
        self.size = self.width, self.height = Var_global.screen_width, Var_global.screen_height
        self.title = "KSOLID Game"
        self._image = None
        self.background_image = None
        self.background_image_rect = None
        self.screen = None

    
    def set_title(self):
        pygame.display.set_caption(self.title)

  
    def set_background_image(self):
        self.background_image = pygame.image.load(self._image).convert()
        self.background_image_rect = self.background_image.get_rect()
        

    def get_background_image(self):
        return self.background_image
    

   
    def display_screen(self):
        self.screen = pygame.display.set_mode(self.size)
    

    
    def get_display_screen(self):
        return self.screen





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

