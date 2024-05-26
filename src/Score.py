import Var_global, pygame
class score:
    def __init__(self, screen, count) -> None:
        self.screen = screen

        self.count = count
        self.x = None
        self.y = None
        self.font_type = Var_global.font_type
        self.font_size = Var_global.font_size_title
        self.font = pygame.font.Font(self.font_type, self.font_size)
        self.text = self.font.render('Puntuación: ' + str(self.count), 1, 'white')

    def set_counter(self, x, y):
        self.x = x
        self.y = y    
        self.screen.blit(self.text, (self.x, self.y)) 

    def update(self, event_list, amount_move):

        if event_list.type == pygame.KEYDOWN:
            self.count -= amount_move 
        return self.count 
    

