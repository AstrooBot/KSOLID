import pygame, Buttons, Var_global , Iscreen, Board, Player, Objects

class screen3(Iscreen.screen): 
    def __init__(self,screen):
        self.board = Board.board(screen)
        self.board.set_board(11,8)
        self.player = Player.player(screen, self.board)
        self.flag = Objects.objects(screen, self.board, 'flag.png')
        self.flag.set_object(809, 639)
        self.water_counter = 0
        self.fire_counter = 0
        super().__init__(screen)
    
    def but_action(self):
        channel = 3
        for i in self.expected_events:

            if i == 'but_map_event':
                self.board.set_board(11,8)
                self.player.rect.centerx = 50 + 35
                self.player.rect.centery = 100 + 35
                self.flag.set_object(809, 639)
            
            if i == 'but_water_object_event':
                if self.player.image_addr == 'kirby_fast.png' or self.player.image_addr == 'kirby_fire_fast.png':
                    self.player.set_image('kirby_water&fast.png')
                else: 
                    self.player.set_image('kirby_water.png')
                self.water_counter += 1

            if i == 'but_fire_object_event' :
                if self.player.image_addr == 'kirby_fast.png' or self.player.image_addr == 'kirby_water&fast.png':
                    self.player.set_image('kirby_fire_fast.png')
                else: 
                    self.player.set_image('kirby_fire.png')
                self.fire_counter += 1
                
            if self.player.rect.x + 10 == self.flag.rect.x and self.player.rect.y + 6 == self.flag.rect.y:
                
                game_over_menu = Buttons.button(self.screen, (153,170,187), 1000, 400)
                game_over_menu.shape(140,160)
                font = pygame.font.Font(None, 70)
                self.screen.blit(font.render('Fin del juego', 1, 'white'), (430, 190))
        return channel
               

    def display(self, event_list):    
        self.reset_events()
        self.board.shape_board()
        self.screen.blit(self.player.imagen, self.player.rect)
        self.screen.blit(self.flag.image, self.flag.rect)

        but_map = buttons3(self.screen, 170, 50)
        but_map.shape(1000, Var_global.screen_height/2)
        but_map.set_text('Mapa')
        but_map_event = self.isHappening(but_map.isClicked(event_list), 'but_map_event')

        but_water_object = buttons3(self.screen, 70, 70)
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

        self.expected_events.append(but_map_event)
        self.expected_events.append(but_water_object_event)
        self.expected_events.append(but_fire_object_event)
        
        

        

        

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
        self.image = None
        

    def set_image(self, image):
        self.image = pygame.image.load(image)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        self.screen.blit(self.image, self.image_rect)
    


    
