import pygame, Var_global


class screen :

    
    def __init__(self, screen):

        self.caption = "KSOLID Game"
        self._image = None
        self.background_image = None
        self.background_image_rect = None
        self.screen = screen
        self.font = pygame.font.Font(Var_global.font_type, Var_global.font_size_title)
        self.expected_events = []

    
    def set_caption(self):
        pygame.display.set_caption(self.caption)
    

    def set_title(self,text):
    
        title = self.font.render(text, 1, Var_global.font_color_title) 
        self.screen.blit(title,(Var_global.screen_width/3, Var_global.screen_height/8))   

  
    def set_background_image(self):
        self.background_image = pygame.image.load(self._image).convert()
        self.background_image_rect = self.background_image.get_rect()
        

    def get_background_image(self):
        return self.background_image
    
    def reset_events(self):
        del self.expected_events[:] 

    def isHappening(self, bool, event_name):
        if bool == True:
            isEvent = event_name
        else: 
            isEvent = None
        return isEvent
 
