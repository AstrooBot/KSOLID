import pygame, Buttons, Var_global , Iscreen

class screen4(Iscreen.screen): 
    def __init__(self,screen):
        super().__init__(screen)
    
    def but_action(self):
        channel = 0
        for i in self.expected_events:
            if i == 'but_rei_event':
                channel = 2
            
            if i == 'but_restart_event':
                channel = 2 
                self.set_data('restart_event')
  
        return channel


    def display(self, event_list):    

        self.reset_events()
        game_over_menu = Buttons.button(self.screen, (153,170,187), 1000, 400)
        game_over_menu.shape(140,160)
        font = pygame.font.Font(None, 70)
        self.screen.blit(font.render(str(self.data), 1, 'white'), (430, 190))

        but_rei = buttons4(self.screen)
        but_rei.shape(50,50)
        but_rei.set_text('reintentar')
        but_rei_event = self.isHappening(but_rei.isClicked(event_list), 'but_rei_event')

        but_restart = buttons4(self.screen)
        but_restart.shape(250,250)
        but_restart.set_text('nuevo mapa')
        but_restart_event = self.isHappening(but_restart.isClicked(event_list), 'but_restart_event')

        self.expected_events.append(but_rei_event)
        self.expected_events.append(but_restart_event)



class buttons4(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = Var_global.button_color
        self.width = 170
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35