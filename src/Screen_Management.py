import pygame, sys 
from Screen1 import *
class Screen_Management:

    def __init__(self, current_screen):
        self.current_screen = current_screen
    
    def set_screen(self, screen):
        self.screen_list = self.current_screen
        return self.current_screen

    def get_screen(self):
        return self.current_screen
    
    def main(self):
        pass