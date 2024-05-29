"""import tkinter

frame = tkinter.Tk()

frame.geometry('500x720')

var = '¿Cómo jugar KSOLID?'
var2 = 'KSOLID es un juego de estrategia en el que debes llegar a la meta con la menor cantidad de movimientos y poderes posibles.' 

label = tkinter.Label(frame, text = var, font = ('monospace', 15) )
label2 = tkinter.Label(frame, text= var2, font= ('monospace', 10))
label.pack()
label2.pack()
frame.mainloop()"""
import tkinter as tk

def ajustar_label():
    texto = entry_texto.get()
    label_texto.config(text=texto)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Texto ajustable")

# Configuración del frame
frame = tk.Frame(root, width=200, height=100)
frame.pack()

# Entrada de texto
entry_texto = tk.Entry(root)
entry_texto.pack()

# Botón para ajustar el texto
boton_ajustar = tk.Button(root, text="Ajustar texto", command=ajustar_label)
boton_ajustar.pack()

# Label para mostrar el texto
label_texto = tk.Label(frame, wraplength=190)  # 190 para dejar un poco de margen
label_texto.pack()
def main():
    root.mainloop()

