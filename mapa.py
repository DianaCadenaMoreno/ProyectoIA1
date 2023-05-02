import tkinter as tk
from PIL import Image, ImageTk

def dibujarMapa(self):
    # Leer la matriz desde el archivo de texto
    with open("matriz.txt", "r") as archivo:
        lineas = archivo.readlines()
        matriz = [list(map(int, linea.strip().split())) for linea in lineas]

    # Definir los valores y las imágenes correspondientes
    self.libre = 0
    self.muro = 1
    self.goku = 2
    self.freezer = 3
    self.cell = 4
    self.semilla = 5
    self.esfera = 6

    self.imgGoku = ImageTk.PhotoImage(Image.open("resources/goku.jpg"))
    self.imgFreezer = ImageTk.PhotoImage(Image.open("resources/freezer.jpg"))
    self.imgCell = ImageTk.PhotoImage(Image.open("resources/cell.jpg"))
    self.imgSemilla = ImageTk.PhotoImage(Image.open("resources/semilla.jpg"))
    self.imgEsfera = ImageTk.PhotoImage(Image.open("resources/esfera.png"))
            
    # Dibujar la matriz en la ventana
    for i in range(10):
        for j in range(10):
            x = j * 60
            y = i * 60
            self.canvas = tk.Canvas(self, width=60, height=60)
            self.canvas.place(x=x, y=y)

            if matriz[i][j] == self.libre:
                self.canvas.create_rectangle(0, 0, 60, 60, fill="white", outline="black")
            elif matriz[i][j] == self.muro:
                self.canvas.create_rectangle(0, 0, 60, 60, fill="orange", outline="black")
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