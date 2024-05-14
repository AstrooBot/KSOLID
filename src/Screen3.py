import pygame, Buttons, Var_global , Iscreen, Board


class screen3(Iscreen.screen): 
    def __init__(self,screen):
        self.board = Board.board(screen)
        self.board.set_board(11,8)
        super().__init__(screen)

    def display(self, event_list):    
        self.reset_events()
        self.board.shape_board()
        but_map = buttons3(self.screen)
        but_map.shape(1100, Var_global.screen_height/2)
        but_map.set_text('Mapa')
        but_map = self.isHappening(but_map.isClicked(event_list), 'but_map_event')
        self.expected_events.append(but_map)


       
        
        

class buttons3(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = Var_global.button_color
        self.width = 170
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35