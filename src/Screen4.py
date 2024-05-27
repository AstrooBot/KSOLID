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
        self.set_title('¡Has llegado a la meta!')

        but_rei = buttons4(self.screen)
        but_rei.shape(25,25)
        but_rei.set_text('Reintentar')
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
        self.width = 140
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35