import Buttons, Var_global , Iscreen, Board, Player, Objects, Score

class screen3(Iscreen.screen): 
    def __init__(self,screen):

        super().__init__(screen)
        self.board = Board.board(screen)
        self.board.set_board(11,8)
        self.player = Player.player(screen, self.board)
        self.flag = Objects.objects(screen, self.board, 'flag.png')
        self.flag.set_object(809, 639)
        self.water_counter = 0
        self.fire_counter = 0
        self.info = []
        self.score_count = Var_global.initial_score
        self.moves = 1
        self.map_bool = False


    
    def display(self, event_list):

        if self.data == 'restart_event':
            self.restart()
            self.data = None  
            self.map_bool = True
        if self.data == 'retry_event':
                self.moves = 1
                self.player.moves = 0
                self.player.len_move = 72
                self.player.rect.centerx = 50 + 35
                self.player.rect.centery = 100 + 35
                self.flag.set_object(809, 639)
                self.score_count = Var_global.initial_score
                self.player.set_image('sprite.png')
                self.water_counter = 0
                self.fire_counter = 0
                self.data = None
                del self.info[:] 
  
        self.reset_events()
        self.board.shape_board()
        self.screen.blit(self.player.imagen, self.player.rect)
        self.screen.blit(self.flag.image, self.flag.rect)

        but_map = buttons3(self.screen, 250, 50)
        but_map.shape(920, Var_global.screen_height/2)
        but_map.set_text('Generar nuevo Mapa')
        but_map_event = self.isHappening(but_map.isClicked(event_list), 'but_map_event')

        but_water_object = buttons3(self.screen, 70, 70)
        but_water_object.color = Var_global.box_water
        but_water_object.shape(1000,450)
        but_water_object.set_image('kirby_water.png')
        but_water_object_event = self.isHappening(but_water_object.isClicked(event_list), 'but_water_object_event')

        but_water_counter = buttons3(self.screen, 70 , 70)
        but_water_counter.shape(1000, 530)
        but_water_counter.set_text(str(self.water_counter))

        but_fire_object = buttons3(self.screen, 70, 70)
        but_fire_object.color = Var_global.box_fire
        but_fire_object.shape(880, 450)
        but_fire_object.set_image('kirby_fire.png')
        but_fire_object_event = self.isHappening(but_fire_object.isClicked(event_list), 'but_fire_object_event')

        but_fire_counter = buttons3(self.screen, 70 , 70)
        but_fire_counter.shape(880, 530)
        but_fire_counter.set_text(str(self.fire_counter))

        score_counter = Score.score(self.screen, self.score_count)
        score_counter.set_counter(250, 20)

        self.expected_events.append(but_map_event)
        self.expected_events.append(but_water_object_event)
        self.expected_events.append(but_fire_object_event)
        self.expected_events.append(self.data)

        self.player.update(event_list)
        self.score_count = score_counter.update(event_list,self.player.box_moved)
        self.moves = self.player.moves
    
    def restart(self):
                self.moves = 1
                self.player.moves = 0
                self.player.len_move = 72
                self.board.set_board(11,8)
                self.player.rect.centerx = 50 + 35
                self.player.rect.centery = 100 + 35
                self.flag.set_object(809, 639)
                self.score_count = Var_global.initial_score
                self.player.set_image('sprite.png')
                self.water_counter = 0
                self.fire_counter = 0
                del self.info[:] 

    def but_action(self):
        channel = 2

        for i in self.expected_events:

            if i == 'but_map_event':
                self.restart() 
                self.map_bool = True      
            if i == 'but_water_object_event':
                if self.player.image_addr == '../images/kirby_fast.png' or self.player.image_addr == '../images/kirby_fire_fast.png':
                    self.player.set_image('kirby_water&fast.png')
                else: 
                    self.player.set_image('kirby_water.png')
                self.water_counter += 1
                self.score_count -= Var_global.box_special_score_normal

            if i == 'but_fire_object_event' :
                if self.player.image_addr == '../images/kirby_fast.png' or self.player.image_addr == '../images/kirby_water&fast.png':
                    self.player.set_image('kirby_fire_fast.png')
                else: 
                    self.player.set_image('kirby_fire.png')
                self.fire_counter += 1
                self.score_count -= Var_global.box_special_score_normal

            if self.player.rect.x + 10 == self.flag.rect.x and self.player.rect.y + 6 == self.flag.rect.y:
                del self.info[:] 
                self.info.append(self.score_count)
                self.info.append(self.water_counter)
                self.info.append(self.fire_counter)
                self.info.append(self.moves)
                self.info.append(self.map_bool)
                self.set_data(self.info) 
                channel = 3
                self.player.rect.centerx = 50 + 35
                self.player.rect.centery = 100 + 35
                self.player.set_image('sprite.png')
                self.score_count = Var_global.initial_score
                self.water_counter = 0
                self.fire_counter = 0
    
        return channel
        
class buttons3(Buttons.button):

    def __init__(self, screen, width, height):
        self.screen = screen
        self.color = Var_global.button_color
        self.width = width
        self.height = height
        super().__init__(self.screen, self.color, self.width, self.height)
        self.text_color = (255,255,255)
        self.text_font_type = Var_global.font_type
        self.text_size = 35

        


    


    
