import pygame, Var_global

class screen :

    def __init__(self, screen):

        self.caption = "KSOLID Game"
        self._image = None
        self.screen = screen
        self.font = pygame.font.Font(Var_global.font_type, Var_global.font_size_title)
        self.expected_events = []
        self.data = None
        self.score = None
        self.score_count = None
        self.high_score = None
        self.player = None
        self.board = None
        self.info = None
        self.map_bool = None
        self.move = None
        self.flag = None
        self.water_counter = None
        self.fire_counter = None

    def set_title(self,text):
    
        title = self.font.render(text, 1, Var_global.font_color_title) 
        self.screen.blit(title,(Var_global.screen_width/3, Var_global.screen_height/8))   
    
    def reset_events(self):
        del self.expected_events[:] 

    def isHappening(self, bool, event_name):
        if bool == True:
            isEvent = event_name
        else: 
            isEvent = None
        return isEvent
    
    def but_action(self):
        return 0
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_text(self, x, y, text):
        ctext = self.font.render(text, 1, Var_global.font_color_title)
        self.screen.blit(ctext, (x, y))
        return ctext
    
    def display(self):
        pass