import tkinter
from PIL import ImageTk, Image
import Var_global

class how_to_play():
    def __init__(self, width, height):
        self.script = []
        self.labels = []
        self.images_to_pack = []
        self.font_type = 'monospace'
        self.font_title_size = '15'
        self.font_body_size = '10'
        self.width = width
        self.height = height
        self.size = str(width) + 'x' + str(height)
        self.frame = tkinter.Tk()
        self.frame.geometry(self.size)
        self.img_width = 450
        self.img_height = 400
        self.img_width1 = 70
        self.img_height1 = 70
        self.canvas = tkinter.Canvas(self.frame, width=self.width - 10 , height=self.height - 10)
        self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar = tkinter.Scrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.inner_frame = tkinter.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=tkinter.NW)

    def convert(self):
        index = 0
        for string in Var_global.how_to_play_script:
            index += 1
            match string[0]:
                case 'T':
                    self.set_title(string[1:])
                case 'I':
                    self.set_image(string[1:], self.img_width, self.img_height)
                case 'B':
                    self.set_body(string[1:])
                case 'N':
                    self.set_image(string[1:], self.img_width1, self.img_height1)
                case 'v':
                    self.set_body('\n')
                case _:
                    self.set_body(string)
                    print('Error at: ' + str(index) + string)

    def set_title(self, text):
        label = tkinter.Label(self.inner_frame, wraplength=self.width, font=(self.font_type, self.font_title_size))
        label.config(text=text)
        label.pack()

    def set_body(self, text):
        label = tkinter.Label(self.inner_frame, wraplength=self.width, font=(self.font_type, self.font_body_size))
        label.config(text=text)
        label.pack()

    def set_image(self, image_addr, width, height):
        image = Image.open(image_addr)
        image = image.resize((width, height))
        image_to_pack = ImageTk.PhotoImage(image)
        self.images_to_pack.append(image_to_pack)
        label_image = tkinter.Label(self.inner_frame, image=image_to_pack)
        label_image.pack()

    def display(self):
        self.frame.mainloop()

def frame_display():
    frame = how_to_play(500, 720)
    frame.script = Var_global.how_to_play_script
    frame.convert()
    frame.display()
