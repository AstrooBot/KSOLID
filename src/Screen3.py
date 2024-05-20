import pygame, Buttons, Var_global , Iscreen, Board, Player

class screen3(Iscreen.screen): 
    def __init__(self,screen):
        self.board = Board.board(screen)
        self.board.set_board(11,8)
        self.player = Player.player(screen, self.board)
        super().__init__(screen)

    def display(self, event_list):    
        self.reset_events()
        self.board.shape_board()
        self.screen.blit(self.player.imagen, self.player.rect)

        but_map = buttons3(self.screen, 170, 50)
        but_map.shape(1100, Var_global.screen_height/2)
        but_map.set_text('Mapa')
        but_map = self.isHappening(but_map.isClicked(event_list), 'but_map_event')

        but_water_object = buttons3(self.screen, 70, 70)
        but_water_object.shape(1000,450)
        but_water_object.set_image('kirby_water.png')

        but_fire_object = buttons3(self.screen, 70, 70)
        but_fire_object.color = Var_global.box_fire
        but_fire_object.shape(880, 450)
        but_fire_object.set_image('kirby_fire.png')

        self.expected_events.append(but_map)
        

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
    


    
