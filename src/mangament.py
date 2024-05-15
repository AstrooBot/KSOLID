import pygame
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
            if i == 'but_map_event' :
                self.current_Screen.board.set_board(11,8)
              
        


  
