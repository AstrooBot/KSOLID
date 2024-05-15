import pygame, sys, mangament, Var_global, Screen1, Screen2, Screen3

"""La siguiente clase almacena la superficie en la que se trabajara todas las pantallas. Es como si main_screen fuera una hoja en blanco
y cada pantalla, una impresion que puede ponerse sobre la hoja. Cada pantalla trabaja sobre las medidas globales pero todas sus solicitudes se
pasan a esta pantalla principal"""

class main_screen: 
     """Por ahora como no exige mas, No es una instancia de la interfaz pantalla"""
     def __init__(self):
          
          """surface es donde se dibuja todo, el lienzo en blanco"""
          
          self.surface = pygame.display.set_mode((Var_global.screen_width,Var_global.screen_height))
          self.gestor = mangament.screen_mangament()

          """Screens es una lista que almacena instancias de cada una de las pantallas. como si hiciera las impresiones de todas las pantallas en
          la hoja"""

          self.screens = [Screen1.screen1(self.surface), Screen2.screen2(self.surface), Screen3.screen3(self.surface)]
          self.gestor.set_screens(self.screens)
          self.gestor.set_current_screen(1)
        
     def update(self, event_list):
         
         """update es el metodo por el cual la pantalla se actualiza en tiempo real. se plantea primero que sea negro, para que borre lo que estaba
         antes"""

         self.surface.fill('Black')

         """Gestor update es donde se gestiona las actualizacion de la pantalla actual"""

         self.gestor.update(event_list)


     def running(self):
        pygame.init()
        while 1:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update(event_list)
            
            pygame.display.update()

def main():
    pygame.init()

    screen = main_screen()
    screen.running()    


if __name__ == '__main__' : 
    main()