import pygame, Buttons
from pygame.locals import *
"""Este codigo se enfoca en ser el gestor de pantalla. le indica a la pantalla principal que y cuando debe dibujar"""
"""Este codigo se ha vuelto el kernel de KSOLID"""
class screen_mangament:

    def __init__(self):    
        self.current_Screen = None
        self.screens = []


    def set_screens(self, screens):

        for i in screens:
           self.screens.append(i)
        
    def set_current_screen(self, index_screen):
        if index_screen == 0:
                self.current_Screen = self.current_Screen
        else:   

            if self.current_Screen != None:
                self.screens[index_screen - 1].set_data(self.current_Screen.data)   
            self.current_Screen = self.screens[index_screen - 1]
                
    

    def get_current_screen(self):
        return self.current_Screen
    
    def update(self, event_list):   
        pygame.display.set_caption(self.current_Screen.caption)
        self.set_current_screen(self.current_Screen.but_action())
        self.current_Screen.display(event_list)

        """Despues de dibujar todo lo que exige la pantalla, el gestor de pantallas verifica que eventos deben haber
        para esto toma la lista de expected_events de la pantalla actual y segun el nombre hace la accion esperable"""


    

     
        




  
