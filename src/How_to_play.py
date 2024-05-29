import tkinter
from PIL import ImageTk, Image
class how_to_play():
    def __init__(self, width, heigth) :

        self.script = []
        self.labels = []
        self.font_type = 'monospace'
        self.font_title_size = '15'
        self.font_body_size = '10'
        self.width = width
        self.height = heigth
        self.size = str(width) + 'x' + str(heigth)
        self.frame = tkinter.Tk()
        self.frame.geometry(self.size)

    def convert(self):

        for string in self.script:

            if string[0] == 'T' :
                self.set_title(string[1:])
            
            elif string[0] == 'I' :
                self.set_image(string[1:])
            
            elif string[0] == 'B' :
                self.set_body(string[1:])
            
            else: 
                self.set_body(string)




 
    
    def set_title(self, text):

        label = tkinter.Label(self.frame, wraplength= self.width,font = (self.font_type, self.font_title_size))
        label.config(text = text)
        self.labels.append(label)
    
    def set_body(self, text):

        label = tkinter.Label(self.frame, wraplength= self.width,font = (self.font_type, self.font_body_size))
        label.config(text = text)
        self.labels.append(label)
    
    def set_image(self, image_addr, width, height):

        image = Image.open(image_addr)
        image = image.resize(width, height)
        image_to_pack = ImageTk.PhotoImage(image)
        label_image = tkinter.Label(self.frame, image = image_to_pack)
        self.labels.append(label_image)
    
    def pack_everything(self):
        
        for element in self.labels :
            element.pack()
    
    def display(self):
        self.frame.mainloop()
        

frame = how_to_play(500, 700)
frame.script = ['Thola']
frame.convert()
frame.pack_everything()
frame.display()


