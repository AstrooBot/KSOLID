import pygame, Var_global
from pygame.locals import *
from pygame.sprite import  Sprite

class player(Sprite):
    def __init__(self, screen, board):
         
         self.contenedor = screen
         self.board = board
         self.image_addr = '../images/sprite.png'
         self.imagen = pygame.image.load(self.image_addr)
         self.rect = self.imagen.get_rect()
         self.rect.centerx = 50 + 35
         self.rect.centery = 100 + 35
         self.len_move = 72
         self.amount_move = 0
         self.box_moved = 0
         self.moves = 0
         super().__init__()
    
    def set_image(self, image_addr):
         self.image_addr = str('../images/'+image_addr)
         self.imagen = pygame.image.load(self.image_addr)

    def update(self, event_list):

        if event_list.type == pygame.KEYDOWN:
          sumar = True
          keys = pygame.key.get_pressed()
          if keys [K_w] and not 'up' in self.track_limits():
  
               self.rect.y -= self.len_move
        
               if self.can_pass() == False:
                         self.rect.y += self.len_move
                         self.len_move = 72
                         self.set_image('sprite.png')
                         self.amount_move = 0
               else: 
                     self.is_power_up()
                     self.amount_move = 1
                     self.moves += 1

          elif keys [ K_w] and 'up' in self.track_limits():
               print('I cannot go up')
               self.len_move = 72 
               self.set_image('sprite.png')
            
          elif keys [K_s] and not 'down' in self.track_limits():
               self.rect.y += self.len_move
 
               if self.can_pass() == False:
                              self.rect.y -= self.len_move
                              self.len_move = 72 
                              self.set_image('sprite.png')
                              self.amount_move = 0
               else: 
                         self.is_power_up()
                         self.amount_move = 1
                         self.moves += 1

          elif keys [ K_s] and 'down' in self.track_limits():
               print('I cannot go down')
               self.len_move = 72 
               self.set_image('sprite.png')

          elif keys [K_a] and not 'left' in self.track_limits():
               self.rect.x -= self.len_move

               if self.can_pass() == False:
                              self.rect.x += self.len_move
                              self.len_move += 72  
                              self.set_image('sprite.png')
                              self.amount_move = 0
               else: 
                         self.is_power_up()
                         self.amount_move = 1
                         self.moves += 1

          elif keys [ K_a] and 'left' in self.track_limits():
               print('I cannot go left')
               self.len_move = 72 
               self.set_image('sprite.png')

          elif keys [K_d] and not 'right' in self.track_limits():
               self.rect.x += self.len_move
               
               if self.can_pass() == False:
                              self.rect.x -= self.len_move
                              self.len_move = 72  
                              self.set_image('sprite.png')
                              self.amount_move = 0
               else: 
                         self.is_power_up()
                         self.amount_move = 1
                         self.moves += 1
          elif keys [ K_d] and 'right' in self.track_limits():
               print('I cannot go right')
               self.len_move = 72 
               self.set_image('sprite.png')

          else: 
                sumar = False
          self.box_moved = sumar * self.amount_move * Var_global.box_neutral_score_normal        
             
    def track_limits(self):
         check = []
         if self.rect.x - 5 <= 50 or self.rect.y - 5 + self.len_move  - 72 <= 50: 
              check.append('left')

         if self.rect.x + 60 + 5 >= 840 or self.rect.y + 65 + self.len_move - 72 >= 840 : 
               check.append('right')

         if self.rect.y - 5 <= 100 :
              check.append('up')

         if self.rect.y + 60 + 5 >= 674 or self.rect.y + 65 + self.len_move  - 72 >= 674 :
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
         if self.get_current_box() == None:
                   check = False
                   print('I cannot go any futher')

         else:                 
            match self.get_current_box().color:
              
              case Var_global.box_fire:
                   
                    if self.image_addr != '../images/kirby_fire.png' and self.image_addr != '../images/kirby_fire_fast.png':
                         check = False
                         print('I cannot pass, there is fire')

              case Var_global.box_water:
                    
                    if self.image_addr != '../images/kirby_water.png' and self.image_addr != '../images/kirby_water&fast.png':
                         check = False
                         print('I cannot pass, there is water')

              case Var_global.box_speed:
                         check = True
     
              case Var_global.box_neutral:
                         check = True
                         if self.len_move > 72: 
                               self.set_image('kirby_fast.png')
                         else:
                               self.set_image('sprite.png')
              case _ : 

                   check = False
         
         return check
    
    def is_power_up(self):
          if self.get_current_box() != None:
               match self.get_current_box().color:
                         
                    case Var_global.box_speed:
     
                                   print('Now I am fast')
                                   self.len_move += 72
                                   self.set_image('kirby_fast.png')

                    case Var_global.box_neutral:

                                   if self.len_move > 72: 
                                        self.set_image('kirby_fast.png')
                                   else:
                                        self.set_image('sprite.png')


