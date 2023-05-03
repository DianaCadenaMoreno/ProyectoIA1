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

        # Texto 3 (Busquedas)
        texto_busqueda = tk.Label(self, text="Seleccione la busqueda", fg="black")
        texto_busqueda.pack()
        texto_busqueda.config(font=('Times New Roman', 12), bg="white")
        texto_busqueda.place(x=610, y=110)

        # DropBox 1 (Busquedas)
        opciones1 = ["Busqueda no informada", "Busqueda informada"]
        variar_opciones1 = tk.StringVar(self)
        variar_opciones1.set(opciones1[0])

        drop_box_busqueda = tk.OptionMenu(self, variar_opciones1, *opciones1)
        drop_box_busqueda.pack()
        drop_box_busqueda.place(x=610, y=140)
        drop_box_busqueda.config(font=('Times New Roman', 10), bg="orange", fg="black")
        
        # DropBox 2 (Busqueda no informada)
        opciones2 = ["Amplitud", "Profundidad", "Costo uniforme"]
        variar_opciones2 = tk.StringVar(self)
        
        # DropBox 3 (Busqueda informada)
        opciones3 = ["Avara", "A*"]
        variar_opciones3 = tk.StringVar(self)
        drop_box_busquedaNO = tk.OptionMenu(self, variar_opciones2, *opciones2)
        drop_box_busquedaIN = tk.OptionMenu(self, variar_opciones3, *opciones3)

        def seleccionarBusqueda():
            busqueda_algoritmo = variar_opciones1.get()

            if busqueda_algoritmo == "Busqueda no informada":
                drop_box_busquedaIN.pack_forget()
                variar_opciones2.set(opciones2[0])     
                drop_box_busquedaNO.pack(side="right", padx=135, pady=[10,150])       
                drop_box_busquedaNO.config(font=('Times New Roman', 10), bg="orange", fg="black") 

            elif busqueda_algoritmo == "Busqueda informada":
                drop_box_busquedaNO.pack_forget()
                variar_opciones3.set(opciones3[0])
                drop_box_busquedaIN.pack(side="right", padx=135, pady=[10,150]) 
                drop_box_busquedaIN.config(font=('Times New Roman', 10), bg="orange", fg="black") 
                
        # Boton para iniciar el algoritmo
        def iniciar_algoritmo():
            BusquedaNoInformada = variar_opciones2.get()
            BusquedaInformada = variar_opciones3.get()
            if BusquedaNoInformada == "Amplitud":
                final = amplitud(matriz)
                movimientosAgente = final[0]
                moverAgente(self,movimientosAgente)
            elif BusquedaNoInformada == "Profundidad":
                pass
            elif BusquedaNoInformada == "Costo uniforme":
                pass
            ###
            if BusquedaInformada == "Avara":
                pass
            elif BusquedaInformada == "A*":
                pass

        # Botón para iniciar el algoritmo seleccionado
        boton_inicio = tk.Button(self, text="Iniciar algoritmo", command=iniciar_algoritmo, bg="black", fg="white")
        boton_inicio.pack()
        boton_inicio.place(x=775, y=215)

        # Botón para seleccionar busqueda
        boton_seleccion = tk.Button(self, text="Seleccionar", command=seleccionarBusqueda, bg="black", fg="white")
        boton_seleccion.pack()
        boton_seleccion.place(x=800, y=140)

        # Label de reporte