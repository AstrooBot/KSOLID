import sys, pygame, Buttons, Var_global, random

class board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.box_list = []
        self.box_list_work = []
        self.fire_boxes = []
        self.water_boxes = []
        self.speed_boxes = []
        self.special_boxes = []
    
    def shape_board(self):
        for i in self.box_list:
            i.shape(i.x, i.y)
    
    def set_type_loza(self, type_box_list, color):
        for i in type_box_list: 
            i.color = color
            self.special_boxes.append(i)
    
    def generate_percentage_boxes(self, percentage_min, percentage_max):
        return int((random.randint(percentage_min - 1, percentage_max + 1)/100)*len(self.box_list_work))
       
    def set_board(self, columnas, filas):

        for j in range(0,filas):

            for i in range(0, columnas):

                box = Box(self.screen)
                box.x = 50+(i*1.5)+(i*70)
                box.y = 100+(j*1.5)+(j*70)
                self.box_list.append(box)

        self.box_list_work = self.box_list[1 : len(self.box_list) - 2]              
        random.shuffle(self.box_list_work)
        
        self.fire_boxes = self.box_list_work[len(self.special_boxes) : self.generate_percentage_boxes(20, 40)]
        self.set_type_loza(self.fire_boxes, Var_global.box_fire)

        self.water_boxes = self.box_list_work[len(self.special_boxes) : len(self.special_boxes) + self.generate_percentage_boxes(20, 40)]
        self.set_type_loza(self.water_boxes, Var_global.box_water)

        self.speed_boxes = self.box_list_work[ len(self.special_boxes) : len(self.special_boxes) + self.generate_percentage_boxes(2, 15)]
        self.set_type_loza(self.speed_boxes, Var_global.box_speed) 

        self.shape_board()

class Box(Buttons.button):

    def __init__(self, screen):
        self.screen = screen
        self.color = Var_global.box_neutral
        self.width = 70
        self.height = self.width
        super().__init__(self.screen, self.color, self.width, self.height)

"""
def main():
        screen = pygame.display.set_mode(size=(1280, 720))
        pygame.init()
        board = board(screen)
        board.set_board(11,8)
        while 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

if __name__ == '__main__':
    main()
"""
