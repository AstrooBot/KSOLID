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
        self.form = None
        self.rect = None

        
    """Este metodo retorna dibujo del boton en la posicion x, y dadas"""
    def shape(self, x, y):
        self.x = x
        self.y = y
        self.form = pygame.draw.rect(self.screen, self.color , (self.x, self.y, self.width, self.height), 0, border_radius=15)
        self.rect = pygame.rect.Rect(self.form)
        
    """Este metodo, pensado para ser sobrecargado almacena lo que se desea que haga el boton cuando sea oprimido
       Para que el metodo funcione se debe agregar la siguiete linea al for que detecta los eventos:
                if event.type == button.event """    


                
    """Metodo para añadir texto dentro del boton"""
    def set_text(self, text):

        font = pygame.font.Font(self.text_font_type, self.text_size)
        ctext = font.render(text, 1, self.text_color)
        #self.screen.blit(ctext, (self.x+self.x/32, self.height/3+self.y))
        self.screen.blit(ctext, (self.x, self.y))
    """Metodo extra por si se quiere cambiar el tipo de evento, el default es cuando se presiona el click izq"""
    def set_event(self,event):
        self.event = event
    

    def isClicked(self, event_list):
        check = False
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.rect.collidepoint(event.pos):
                    check = True
        return check
"""Este método retorna un booleano cuando el boton en cuestion es presionado con el click izq. Si fue presionado retorna True sino retorna False
   event_list surge de pygame.event.get() y es donde se almacena todos los eventos que detecta pygame, de este se pregunta si se clickeo y si
   fue asi, se pregunta si la posicion en la que se clickeo es la misma al rect del boton en cuestion.
   event_list proviene de la instancia de clase en la que se este trabajando """
    