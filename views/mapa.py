import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import time

with open("resources/maps/matriz.txt", "r") as archivo:
    lineas = archivo.readlines()
    matriz = np.array([list(map(int, linea.strip().split())) for linea in lineas])

def dibujarMapa(self):

    # Definir los valores y las imágenes correspondientes
    self.libre = 0
    self.muro = 1
    self.goku = 2
    self.freezer = 3
    self.cell = 4
    self.semilla = 5
    self.esfera = 6

    self.imgGoku = ImageTk.PhotoImage(Image.open("resources/images/goku.jpg"))
    self.imgFreezer = ImageTk.PhotoImage(Image.open("resources/images/freezer.jpg"))
    self.imgCell = ImageTk.PhotoImage(Image.open("resources/images/cell.jpg"))
    self.imgSemilla = ImageTk.PhotoImage(Image.open("resources/images/semilla.jpg"))
    self.imgEsfera = ImageTk.PhotoImage(Image.open("resources/images/esfera.png"))
            
    # Dibujar la matriz en la ventana
    for i in range(10):
        for j in range(10):
            x = j * 60
            y = i * 60
            self.canvas = tk.Canvas(self, width=60, height=60, bg="white", highlightthickness=1, highlightbackground="black")
            self.canvas.place(x=x, y=y)

            if matriz[i][j] == self.libre:
                self.canvas.create_rectangle(0, 0, 60, 60, fill="white")
            elif matriz[i][j] == self.muro:
                self.canvas.create_rectangle(0, 0, 60, 60, fill="orange")
            elif matriz[i][j] == self.goku:
                self.canvas.create_image(0, 0, image=self.imgGoku, anchor="nw")
            elif matriz[i][j] == self.freezer:
                self.canvas.create_image(0, 0, image=self.imgFreezer, anchor="nw")
            elif matriz[i][j] == self.cell:
                self.canvas.create_image(0, 0, image=self.imgCell, anchor="nw")
            elif matriz[i][j] == self.semilla:
                self.canvas.create_image(0, 0, image=self.imgSemilla, anchor="nw")
            elif matriz[i][j] == self.esfera:
                self.canvas.create_image(0, 0, image=self.imgEsfera, anchor="nw")

def moverAgente(self, ruta):
    self.canvas = None
    self.imgGoku = None
    self.imagen_goku = None

    # crear instancia de lienzo si aún no ha sido creada
    if not self.canvas:
        self.canvas = tk.Canvas(self, width=600, height=600, bg="black", highlightthickness=0)
        self.canvas.pack()
        

    # cargar imagen de Goku si aún no ha sido cargada
    if not self.imgGoku:
        self.imgGoku = ImageTk.PhotoImage(Image.open("resources/images/goku.jpg"))

    # crear imagen de Goku en la posición inicial
    x, y = ruta[0]
    x_pixeles = y * 60
    y_pixeles = x * 60
    self.imagen_goku = self.canvas.create_image(y_pixeles, x_pixeles, image=self.imgGoku, anchor="nw")

    # seguir ruta
    for i in range(1, len(ruta)):
        # obtener posición actual de Goku en la matriz
        x1, y1 = ruta[i-1]

        # obtener posición siguiente de Goku en la matriz
        x2, y2 = ruta[i]

        # calcular la posición de Goku en píxeles para ambos puntos
        x1_pixeles = y1 * 60
        y1_pixeles = x1 * 60
        x2_pixeles = y2 * 60
        y2_pixeles = x2 * 60

        # animación para mover Goku gradualmente desde la posición actual a la siguiente posición
        for t in range(0, 100, 5):
            x_pixeles = x1_pixeles + ((x2_pixeles - x1_pixeles) * t // 100)
            y_pixeles = y1_pixeles + ((y2_pixeles - y1_pixeles) * t // 100)
            self.canvas.coords(self.imagen_goku, y_pixeles, x_pixeles)
            self.update_idletasks()
            time.sleep(0.02)

    # eliminar imagen de Goku del lienzo cuando se termina el recorrido
    self.canvas.delete(self.imagen_goku)