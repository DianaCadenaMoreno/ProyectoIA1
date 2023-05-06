import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import time
# from main import GokuSmart

with open("resources/maps/matriz.txt", "r") as archivo:
    lineas = archivo.readlines()
    matriz = np.array([list(map(int, linea.strip().split()))
                      for linea in lineas])


def moverAgente_mapa(self, ruta):
    # Definir los valores y las imágenes correspondientes
    self.libre = 0
    self.muro = 1
    self.goku = 2
    self.freezer = 3
    self.cell = 4
    self.semilla = 5
    self.esfera = 6

    self.imgGoku = ImageTk.PhotoImage(Image.open("resources/images/goku.jpg"))
    self.imgFreezer = ImageTk.PhotoImage(
        Image.open("resources/images/freezer.jpg"))
    self.imgCell = ImageTk.PhotoImage(Image.open("resources/images/cell.jpg"))
    self.imgSemilla = ImageTk.PhotoImage(
        Image.open("resources/images/semilla.jpg"))
    self.imgEsfera = ImageTk.PhotoImage(
        Image.open("resources/images/esfera.png"))
    img_batallaCell = ImageTk.PhotoImage(
        Image.open("resources/images/batalla_cell.png"))
    img_batallaFree = ImageTk.PhotoImage(
        Image.open("resources/images/batalla_freezer.png"))

    # Crear el canvas
    self.canvas = tk.Canvas(self, width=600, height=600, bg="white")
    self.canvas.place(x=0, y=0)

    # Dibujar la matriz en el canvas
    for i in range(10):
        for j in range(10):
            x = j * 60
            y = i * 60

            if matriz[i][j] == self.libre:
                self.canvas.create_rectangle(x, y, x+60, y+60, fill="white")
            elif matriz[i][j] == self.muro:
                self.canvas.create_rectangle(x, y, x+60, y+60, fill="orange")
            elif matriz[i][j] == self.goku:
                pass
            elif matriz[i][j] == self.freezer:
                self.canvas.create_image(
                    x, y, image=self.imgFreezer, anchor="nw")
            elif matriz[i][j] == self.cell:
                self.canvas.create_image(x, y, image=self.imgCell, anchor="nw")
            elif matriz[i][j] == self.semilla:
                self.canvas.create_image(
                    x, y, image=self.imgSemilla, anchor="nw")
            elif matriz[i][j] == self.esfera:
                self.canvas.create_image(
                    x, y, image=self.imgEsfera, anchor="nw")

    # Cargar imagen original de Goku, batalla de cell y batalla de freezer
    img_goku = Image.open("resources/images/goku.jpg")

    # Redimensionar imagen a píxeles
    img_goku_resized = img_goku.resize((50, 50))

    # Crear objeto ImageTk para la imagen redimensionada
    img_goku_tk = ImageTk.PhotoImage(img_goku_resized)

    # Crear imagen de Goku en la posición inicial
    x, y = ruta[0]
    x_pixeles = y * 60
    y_pixeles = x * 60
    self.imagen_goku = self.canvas.create_image(
        y_pixeles, x_pixeles, image=img_goku_tk, anchor="nw")
    # Variable para indicar si Goku ya ha recogido la semilla
    # Inicializar el acumulador de semillas y esferas
    semillas = 0
    esferas = 0

    # Recorrer la ruta
    for i in range(1, len(ruta)):
        # Obtener posición actual de Goku en la matriz
        x1, y1 = ruta[i-1]

        # Obtener posición siguiente de Goku en la matriz
        x2, y2 = ruta[i]

        # Verificar si hay una semilla en la posición actual de Goku
        if matriz[y1][x1] == self.semilla:
            # Incrementar el contador de semillas
            semillas += 1

        # Verificar si Goku puede eliminar a Cell o Freezer
        if semillas > 0:
            if matriz[y2][x2] == self.cell:
                # Eliminar la imagen correspondiente de la celda
                x_pixeles = y2 * 60
                y_pixeles = x2 * 60
                self.canvas.delete(self.imgCell)
                self.canvas.create_image(
                    y_pixeles, x_pixeles, image=img_batallaCell, anchor="nw")
                # Decrementar el contador de semillas
                semillas -= 1

            elif matriz[y2][x2] == self.freezer:
                # Eliminar la imagen correspondiente de la celda
                x_pixeles = y2 * 60
                y_pixeles = x2 * 60
                self.canvas.delete(self.imgFreezer)
                self.canvas.create_image(
                    y_pixeles, x_pixeles, image=img_batallaFree, anchor="nw")
                # Decrementar el contador de semillas
                semillas -= 1

        else:
            pass

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
