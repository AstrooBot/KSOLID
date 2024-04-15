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
        self.x = None
        self.y = None
        self.text_color = None
        self.text_size = None
        self.text_font_type = None

        
    """Este metodo retorna dibujo del boton en la posicion x, y dadas"""
    def shape(self, x, y):
        self.x = x
        self.y = y
        pygame.draw.rect(self.screen, self.color , (x, y, self.width, self.height), 0, border_radius=15)
        
    """Este metodo, pensado para ser sobrecargado almacena lo que se desea que haga el boton cuando sea oprimido
       Para que el metodo funcione se debe agregar la siguiete linea al for que detecta los eventos:
                if event.type == button.event """    

    def on_click(self):
                self.event = pygame.MOUSEBUTTONDOWN
                self.screen.fill('black')
                #screen.blit()
                
    """Metodo para añadir texto dentro del boton"""
    def set_text(self, text):

        font = pygame.font.Font(self.text_font_type, self.text_size)
        ctext = font.render(text, 1, self.text_color)
        #self.screen.blit(ctext, (self.x+self.x/32, self.height/3+self.y))
        self.screen.blit(ctext, (self.x, self.y))
    """Metodo extra por si se quiere cambiar el tipo de evento, el default es cuando se presiona el click izq"""
    def set_event(self,event):
        self.event = event