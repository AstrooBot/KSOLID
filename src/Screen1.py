import Buttons, Var_global , Iscreen, How_to_play

class screen1(Iscreen.screen): 
    def __init__(self,screen):
        super().__init__(screen)

    def but_action(self):
        channel = 0
        for i in self.expected_events:
            if i == 'but_start_event':
                channel = 2
            if i == 'but_es_event':
                How_to_play.frame_display()
          
        return channel

    def display(self, event_list):    

        self.reset_events()

        self.set_title('Bienvenido a KSOLID')
        but_start = buttons1(self.screen)
        but_start.shape(Var_global.screen_width/2-but_start.width/2,Var_global.screen_height/2-but_start.height/2)
        but_start.set_text('Jugar')

        but_es = buttons1(self.screen)
        but_es.shape(Var_global.screen_width/2-but_start.width/2, Var_global.screen_height*3/4-but_es.height/2)
        but_es.set_text('Como jugar')

        but_start_event = self.isHappening(but_start.isClicked(event_list), 'but_start_event')
        but_es_event = self.isHappening(but_es.isClicked(event_list), 'but_es_event' )

        self.expected_events.append(but_start_event)
        self.expected_events.append(but_es_event)

class buttons1(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = Var_global.button_color
        self.width = 170
        self.height = 50
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35
