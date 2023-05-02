import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from views.mapa import dibujarMapa, moverAgente
from algoritmos.Amplitud import amplitud

with open("resources/maps/matriz.txt", "r") as archivo:
    lineas = archivo.readlines()
    matriz = np.array([list(map(int, linea.strip().split())) for linea in lineas])

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Goku Smart")
        self.geometry("900x600")
        self.config(bg="white")

        # Imagen de titulo
        img = Image.open("resources/images/titulo.png")
        img = img.resize((300, 100)) # Resize the image
        self.photo = ImageTk.PhotoImage(img)
        self.tituloGoku = tk.Label(self, image=self.photo)
        self.tituloGoku.pack(pady=10)
        self.tituloGoku.config(bg="white")
        self.tituloGoku.place(x=600, y=0)

        dibujarMapa(self)

        # Texto 3
        texto_drop = tk.Label(self, text="Seleccione el algoritmo", fg="black")
        texto_drop.pack()
        texto_drop.config(font=('Times New Roman', 12), bg="white")
        texto_drop.place(x=610, y=110)

        # DropBox
        opciones = ["Amplitud", "Costo uniforme", "Profudidad","Avara", "A*"]
        variar_opciones = tk.StringVar(self)
        variar_opciones.set(opciones[0])

        drop_box = tk.OptionMenu(self, variar_opciones, *opciones)
        drop_box.pack()
        drop_box.place(x=610, y=140)
        drop_box.config(font=('Times New Roman', 10), bg="orange", fg="black")

        # Boton para iniciar el algoritmo
        def iniciar_algoritmo():
            algoritmo_seleccionado = variar_opciones.get()
            if algoritmo_seleccionado == "Amplitud":
                final = amplitud(matriz)
                movimientosAgente = final[0]
                moverAgente(self,movimientosAgente)

        # Botón para iniciar el algoritmo seleccionado
        boton_inicio = tk.Button(self, text="Iniciar algoritmo", command=iniciar_algoritmo, bg="black", fg="white")
        boton_inicio.pack()
        boton_inicio.place(x=750, y=140)

        # Label de reporte