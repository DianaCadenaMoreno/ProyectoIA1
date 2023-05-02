import tkinter as tk
from views.mapa import dibujarMapa

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Goku Smart")
        self.geometry("900x600")
        self.config(bg="white")

        self.tituloGoku = tk.Label(self, text="Goku Smart")
        self.tituloGoku.pack(pady=10)
        self.tituloGoku.config(font=("Verdana", 16), fg="black", bg="white")
        self.tituloGoku.place(x=700, y=30)

       
        dibujarMapa(self)
        
       