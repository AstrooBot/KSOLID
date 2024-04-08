"""Objective: dev the differents screens"""
import pygame, sys

pygame.init()
size = 800,800
screen_init = pygame.display.set_mode(size)

#encapsular despues

class button():

    def __init__(self, color,  width, height):
        self.color = color
        self.width = width
        self.height = height
        pygame.draw.rect(screen_init, self.color , [0, 0, self.width, self.height], 0)

    def on_click(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen_init.fill('black')
                pygame.draw.rect(screen_init, self.color , [100, 100, self.width, self.height], 0)
                

but1 = button((0,0,255),100,150)

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            but1.on_click(event)

        pygame.display.update()
        

if __name__ == "__main__":
    main()
    
    
