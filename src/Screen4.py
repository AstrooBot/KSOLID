import Buttons, Var_global , Iscreen

class screen4(Iscreen.screen): 
    def __init__(self,screen):
        super().__init__(screen)
        self.score = None
        self.high_score = None

    def set_high_score(self, new_score):

        if self.high_score == None or self.high_score < new_score:
            self.high_score = new_score
            
    def but_action(self):
        channel = 0
        for i in self.expected_events:
            if i == 'but_rei_event':
                channel = 2
                self.set_data('retry_event')
            
            if i == 'but_restart_event':
                channel = 2 
                self.high_score = 0
                self.set_data('restart_event')
                self.score = None
                self.high_score = None
   
        return channel

    def display(self, event_list):    

        self.reset_events()
        self.set_title('¡Has llegado a la meta!')

        label1 = self.set_text(Var_global.screen_width * 1/3 - 160, Var_global.screen_height * 2/8,'Usaste :')
        label1_rect = label1.get_rect()

        label1_len = Var_global.screen_width * 1/3 - 160

        but_water_object = Buttons.button(self.screen, Var_global.box_water, 70, 70)
        but_water_object.shape(label1_len + label1_rect.topright[0] + 20, Var_global.screen_height * 2/8)
        but_water_object.set_image('kirby_water.png')

        label1_len += label1_rect.topright[0] + 20 

        label1a = self.set_text(but_water_object.rect.left + 80, Var_global.screen_height * 2/8,'x ' + str(self.data[1]))
        label1_len += 80 
        label1a_rect = label1a.get_rect()
        
        but_fire_object = Buttons.button(self.screen,Var_global.box_fire, 70, 70)
        but_fire_object.shape(label1_len + label1a_rect.left + 70, Var_global.screen_height * 2/8)
        but_fire_object.set_image('kirby_fire.png')
        label1b = self.set_text(but_fire_object.rect.left + 80, Var_global.screen_height * 2/8,'x' + str(self.data[2]))

        label2 = self.set_text(Var_global.screen_width * 1/3 - 160, Var_global.screen_height * 3/8,'Moviste :')
        label2_rect = label2.get_rect()

        label2_len = Var_global.screen_width * 1/3 - 160

        box_neutral = Buttons.button(self.screen, Var_global.box_neutral, 70, 70)
        box_neutral.shape(label2_len + label2_rect.topright[0], Var_global.screen_height * 3/8 - 5 )
        box_neutral.set_image('sprite.png')

        label2a = self.set_text(box_neutral.rect.left + 80, Var_global.screen_height * 3/8 - 5,'x '+ str(self.data[3]))

        recta = Buttons.button(self.screen, 'white', 2240 / 3, 5)
        recta.shape(Var_global.screen_width * 1/3 - 160, Var_global.screen_height * 4/8 - 20)

        self.set_text(Var_global.screen_width * 1/3 - 160, Var_global.screen_height * 4/8, 'Puntuación : ' + str(self.score))
        self.set_text(Var_global.screen_width * 1/3 - 160, Var_global.screen_height * 5/8, 'Mejor Puntuación : ' + str(self.high_score))

        but_rei = buttons4(self.screen)
        but_rei.shape(Var_global.screen_width * 1/3 - but_rei.width,Var_global.screen_height * 6/8)
        but_rei.set_text('Reintentar')
        but_rei_event = self.isHappening(but_rei.isClicked(event_list), 'but_rei_event')

        but_restart = buttons4(self.screen)
        but_restart.shape(Var_global.screen_width * 2/3,Var_global.screen_height * 6/8)
        but_restart.set_text('Nuevo mapa')
        but_restart_event = self.isHappening(but_restart.isClicked(event_list), 'but_restart_event')

        self.expected_events.append(but_rei_event)
        self.expected_events.append(but_restart_event)

        self.score = self.data[0] 
        self.set_high_score(self.score)


class buttons4(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = Var_global.button_color
        self.width = 160
        self.height = 80
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35