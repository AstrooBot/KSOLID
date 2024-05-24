import pygame, Buttons
from pygame.locals import *
"""Este codigo se enfoca en ser el gestor de pantalla. le indica a la pantalla principal que y cuando debe dibujar"""

class screen_mangament:

    def __init__(self):    
        self.current_Screen = None
        self.screens = []

    def set_screens(self, screens):

        for i in screens:
           self.screens.append(i)
        
    def set_current_screen(self, index_screen):
        self.current_Screen = self.screens[index_screen-1]
        

    def get_current_screen(self):
        return self.current_Screen
    
    def update(self, event_list):   
        pygame.display.set_caption(self.current_Screen.caption)
        self.current_Screen.display(event_list)
        """Despues de dibujar todo lo que exige la pantalla, el gestor de pantallas verifica que eventos deben haber
        para esto toma la lista de expected_events de la pantalla actual y segun el nombre hace la accion esperable"""
        for i in self.current_Screen.expected_events:
            if i == 'but_start_event':
                self.set_current_screen(3)
            if i == 'but_map_event' and self.current_Screen == self.screens[2] :
                self.current_Screen.board.set_board(11,8)
                self.current_Screen.player.rect.centerx = 50 + 35
                self.current_Screen.player.rect.centery = 100 + 35
                self.current_Screen.flag.set_object(809, 639)
            
            if i == 'but_water_object_event' and self.current_Screen == self.screens[2] :
                if self.current_Screen.player.image_addr == 'kirby_fast.png' or self.current_Screen.player.image_addr == 'kirby_fire_fast.png':
                    self.current_Screen.player.set_image('kirby_water&fast.png')
                else: 
                    self.current_Screen.player.set_image('kirby_water.png')
                self.current_Screen.water_counter += 1

            if i == 'but_fire_object_event'and self.current_Screen == self.screens[2] :
                if self.current_Screen.player.image_addr == 'kirby_fast.png' or self.current_Screen.player.image_addr == 'kirby_water&fast.png':
                    self.current_Screen.player.set_image('kirby_fire_fast.png')
                else: 
                    self.current_Screen.player.set_image('kirby_fire.png')
                self.current_Screen.fire_counter += 1
                
            if self.current_Screen == self.screens[2] and self.current_Screen.player.rect.x + 10 == self.current_Screen.flag.rect.x and self.current_Screen.player.rect.y + 6 == self.current_Screen.flag.rect.y:
                
                game_over_menu = Buttons.button(self.current_Screen.screen, (153,170,187), 1000, 400)
                game_over_menu.shape(140,160)
                font = pygame.font.Font(None, 70)
                self.current_Screen.screen.blit(font.render('Fin del juego', 1, 'white'), (430, 190))
               


  
