import pygame

"""Este codigo esta hecho unicamente para la clase boton"""

class button():

    """atrbutos requeridos para cualquier instancia o clase hija"""
    def __init__(self, screen, color, width, height):
        self.screen = screen
        self.event = None
        self.color = color
        self.width = width
        self.height = height

        
    """Este metodo retorna dibujo del boton en la posicion x, y dadas"""
    def shape(self, x, y):
        pygame.draw.rect(self.screen, self.color , (x, y, self.width, self.height), 0, border_radius=15)
        
    """Este metodo, pensado para ser sobrecargado almacena lo que se desea que haga el boton cuando sea oprimido
       Para que el metodo funcione se debe agregar la siguiete linea al for que detecta los eventos:
                if event.type == button.event """    

    def on_click(self):
                self.event = pygame.MOUSEBUTTONDOWN
                self.screen.fill('black')
                #screen.blit()
                
    """Metodo para añadir texto dentro del boton"""
    def set_text(self, text, color, size, font_type):

        font = pygame.font.Font(font_type, size)
        ctext = font.render(text, 1, color)
        self.screen.blit(ctext, ((2*self.x+self.width)/2, (2*self.y+self.height)/1.75))

    """Metodo extra por si se quiere cambiar el tipo de evento, el default es cuando se presiona el click izq"""
    def set_event(self,event):
        self.event = event