import tkinter as tk
from mapa import dibujarMapa

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Goku Smart")
        self.geometry("900x900")

        self.tituloGoku = tk.Label(self, text="Goku Smart")
        self.tituloGoku.pack(pady=10)
        self.tituloGoku.config(font=("Verdana", 16))

       
        dibujarMapa(self)
        
       