"""Objective: dev the differents screens"""
import pygame, sys

pygame.init()
size = 800,800
screen_init = pygame.display.set_mode(size)

#encapsular despues

class button():

    def __init__(self, color, x , y , width, height):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.shape(self.x,self.y)

    
    def shape(self, x, y):
        pygame.draw.rect(screen_init, self.color , [x, y, x+self.width, y+self.height], 0)
        
        

    def on_click(self, screen, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill('black')
                #screen.blit()
 

    def set_text(self, text, color, screen, size):

        font = pygame.font.Font(None, size)
        ctext = font.render(text, 1, color)
        screen.blit(ctext, ((2*self.x+self.width)/2, (2*self.y+self.height)/1.75))
    






but1 = button((0,0,255), 100, 100, 100, 100)
but1.set_text('hello', (255,255,255), screen_init, 25)


def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            but1.on_click(screen_init , event)

        pygame.display.update()
        

if __name__ == "__main__":
    main()
    
    
