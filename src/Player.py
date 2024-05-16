import pygame, sys, Board, Var_global
from pygame.locals import *
from pygame.sprite import  Sprite

class player(Sprite):
    def __init__(self, screen, board):
         self.contenedor = screen
         self.board = board
         self.imagen = pygame.image.load('sprite.png')
         self.rect = self.imagen.get_rect()
         self.rect.centerx = 50 + 35
         self.rect.centery = 100 + 35
         super().__init__()

    def update(self):
          
          keys = pygame.key.get_pressed()

          if keys [K_w] and not 'up' in self.track_limits():
               self.rect.y -= 72
               if self.can_pass() == False:
                    self.rect.y += 72

          if keys [K_s] and not 'down' in self.track_limits():
               self.rect.y += 72
               if self.can_pass() == False:
                    self.rect.y -= 72

          if keys [K_a] and not 'left' in self.track_limits():
               self.rect.x -= 72 
               if self.can_pass() == False:
                    self.rect.x += 72

          if keys [K_d] and not 'right' in self.track_limits():
               self.rect.x += 72
               if self.can_pass() == False:
                    self.rect.x -= 72
          if keys [K_o]:
               print(self.get_current_box().color)
     
    def track_limits(self):
         check = []
         if self.rect.x - 5 == 50: 
              check.append('left')
         if self.rect.x + 60 + 5 == 840: 
               check.append('right')
         if self.rect.y - 5 == 100:
              check.append('up')
         if self.rect.y + 60 + 5 == 674:
              check.append('down')
         return check
    
    def get_current_box(self):
         current_box = None
         for i in self.board.box_list:
              if i.x == self.rect.x - 5 and i.y == self.rect.y - 5:
                  current_box = i 
         return current_box
    
    def can_pass(self):
         check = True
         if self.get_current_box().color == Var_global.box_fire:
              check = False
              print('I cannot pass, there is fire')

         if self.get_current_box().color == Var_global.box_water:
              check = False
              print('I cannot pass, there is water')

         if self.get_current_box().color == Var_global.box_speed:
              print('Now I am fast')

         if self.get_current_box().color == Var_global.box_neutral:
              print('yeah, I touch some grass :D')
         return check
   

         
          


def main():
    screen = pygame.display.set_mode(size=(1280,720))
    voard = Board.board(screen)
    voard.set_board(11,8)
    kirby = player(screen, voard)
    
    pygame.init()

    while 1:
        screen.fill('black')
        voard.shape_board()
       
        screen.blit(kirby.imagen, kirby.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                kirby.update()
        
        
        pygame.display.update()


