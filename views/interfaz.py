import tkinter as tk
from tkinter import filedialog
import numpy as np
import winsound
import time
from PIL import Image, ImageTk
from views.mapa import moverAgente_mapa
from algoritmos.Amplitud import amplitud
from algoritmos.Profundidad import profundidad
from algoritmos.Costo_uniforme import costo_uniforme
from algoritmos.Avara import avara
from algoritmos.A_estrella import A_estrella


class Interfaz(tk.Tk):

    global matriz

    with open("resources/maps/prueba.txt", "r") as archivo:
        lineas = archivo.readlines()
        matriz = np.array([list(map(int, linea.strip().split()))
                          for linea in lineas])

    def sound(self):
        winsound.PlaySound('resources/sound/esferas.wav',
                           winsound.SND_ASYNC | winsound.SND_LOOP)

    def stop_sound(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)

    def __init__(self):
        super().__init__()
        self.title("Goku Smart")
        self.geometry("900x600")
        self.config(bg="white")

        def inhabilitarSeleccion():
            boton_seleccion.configure(state='disabled')

        def inhabilitarAlgoritmo():
            boton_inicio.configure(state='disabled')

        # Imagen de titulo
        img = Image.open("resources/images/titulo.png")
        img = img.resize((300, 100))  # Resize the image
        self.photo = ImageTk.PhotoImage(img)
        self.tituloGoku = tk.Label(self, image=self.photo)
        self.tituloGoku.pack(pady=10)
        self.tituloGoku.config(bg="white")
        self.tituloGoku.place(x=600, y=0)

        # Texto 3 (Busquedas)
        texto_busqueda = tk.Label(
            self, text="Seleccione la busqueda", fg="black")
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
        drop_box_busqueda.config(
            font=('Times New Roman', 10), bg="orange", fg="black")

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
                drop_box_busquedaNO.pack(
                    side="right", padx=135, pady=[10, 150])
                drop_box_busquedaNO.config(
                    font=('Times New Roman', 10), bg="orange", fg="black")

            elif busqueda_algoritmo == "Busqueda informada":
                drop_box_busquedaNO.pack_forget()
                variar_opciones3.set(opciones3[0])
                drop_box_busquedaIN.pack(
                    side="right", padx=135, pady=[10, 150])
                drop_box_busquedaIN.config(
                    font=('Times New Roman', 10), bg="orange", fg="black")

        # Crear un canvas en la ventana principal
        reporte = tk.Canvas(self, width=300, height=200, bg='white', bd=0)
        reporte.pack()
        reporte.place(x=600, y=300)
        label_reporte = tk.Label(
            reporte, text="Reporte:", fg='black', bg="white", font=('Arial', 12))
        label_reporte.place(x=10, y=10)

        # Boton para iniciar el algoritmo
        def iniciar_algoritmo():
            BusquedaNoInformada = variar_opciones2.get()
            BusquedaInformada = variar_opciones3.get()
            if BusquedaNoInformada == "Amplitud":
                self.sound()
                inicioT = time.time()
                final = amplitud(matriz)
                finalT = time.time()
                movimientosAgente = final[0]
                moverAgente_mapa(self, movimientosAgente)
                self.nodosExpandidos = str(final[1])
                self.profundidadArbol = str(final[2])
                self.tiempo_computo = str(round(finalT - inicioT, 5))
                label_nodos = tk.Label(
                    reporte, text=f'Nodos expandidos: {self.nodosExpandidos}', fg='black', bg="white", font=('Arial', 12))
                label_nodos.place(x=10, y=50)

                label_profundidad = tk.Label(
                    reporte, text=f'Profundidad: {self.profundidadArbol}', fg='black', bg="white", font=('Arial', 12))
                label_profundidad.place(x=10, y=100)

                label_tiempo = tk.Label(
                    reporte, text=f'Tiempo de computo: {self.tiempo_computo} s', fg='black', bg="white", font=('Arial', 12))
                label_tiempo.place(x=10, y=150)
                self.stop_sound()
            elif BusquedaNoInformada == "Profundidad":
                self.sound()
                inicioT = time.time()
                final = profundidad(matriz)
                finalT = time.time()
                movimientosAgente = final[0]
                moverAgente_mapa(self, movimientosAgente)
                self.nodosExpandidos = str(final[1])
                self.profundidadArbol = str(final[2])
                self.tiempo_computo = str(round(finalT - inicioT, 5))
                label_nodos = tk.Label(
                    reporte, text=f'Nodos expandidos: {self.nodosExpandidos}', fg='black', bg="white", font=('Arial', 12))
                label_nodos.place(x=10, y=50)

                label_profundidad = tk.Label(
                    reporte, text=f'Profundidad: {self.profundidadArbol}', fg='black', bg="white", font=('Arial', 12))
                label_profundidad.place(x=10, y=100)

                label_tiempo = tk.Label(
                    reporte, text=f'Tiempo de computo: {self.tiempo_computo} s', fg='black', bg="white", font=('Arial', 12))
                label_tiempo.place(x=10, y=150)
                self.stop_sound()
            elif BusquedaNoInformada == "Costo uniforme":
                self.sound()
                inicioT = time.time()
                final = costo_uniforme(matriz)
                finalT = time.time()
                movimientosAgente = final[0]
                moverAgente_mapa(self, movimientosAgente)
                self.nodosExpandidos = str(final[1])
                self.profundidadArbol = str(final[2])
                self.tiempo_computo = str(round(finalT - inicioT, 5))
                self.costo = str(final[3])
                label_nodos = tk.Label(
                    reporte, text=f'Nodos expandidos: {self.nodosExpandidos}', fg='black', bg="white", font=('Arial', 12))
                label_nodos.place(x=10, y=50)

                label_profundidad = tk.Label(
                    reporte, text=f'Profundidad: {self.profundidadArbol}', fg='black', bg="white", font=('Arial', 12))
                label_profundidad.place(x=10, y=80)

                label_tiempo = tk.Label(
                    reporte, text=f'Tiempo de computo: {self.tiempo_computo} s', fg='black', bg="white", font=('Arial', 12))
                label_tiempo.place(x=10, y=110)

                label_costo = tk.Label(
                    reporte, text=f'Costo: {self.costo}', fg='black', bg="white", font=('Arial', 12))
                label_costo.place(x=10, y=150)
                self.stop_sound()
            if BusquedaInformada == "Avara":
                self.sound()
                inicioT = time.time()
                final = avara(matriz)
                finalT = time.time()
                movimientosAgente = final[0]
                moverAgente_mapa(self, movimientosAgente)
                self.nodosExpandidos = str(final[1])
                self.profundidadArbol = str(final[2])
                self.tiempo_computo = str(round(finalT - inicioT, 5))
                label_nodos = tk.Label(
                    reporte, text=f'Nodos expandidos: {self.nodosExpandidos}', fg='black', bg="white", font=('Arial', 12))
                label_nodos.place(x=10, y=50)

                label_profundidad = tk.Label(
                    reporte, text=f'Profundidad: {self.profundidadArbol}', fg='black', bg="white", font=('Arial', 12))
                label_profundidad.place(x=10, y=100)

                label_tiempo = tk.Label(
                    reporte, text=f'Tiempo de computo: {self.tiempo_computo} s', fg='black', bg="white", font=('Arial', 12))
                label_tiempo.place(x=10, y=150)
                self.stop_sound()
            elif BusquedaInformada == "A*":
                self.sound()
                inicioT = time.time()
                final = A_estrella(matriz)
                finalT = time.time()
                movimientosAgente = final[0]
                moverAgente_mapa(self, movimientosAgente)
                self.nodosExpandidos = str(final[1])
                self.profundidadArbol = str(final[2])
                self.tiempo_computo = str(round(finalT - inicioT, 5))
                self.costo = str(final[3])
                label_nodos = tk.Label(
                    reporte, text=f'Nodos expandidos: {self.nodosExpandidos}', fg='black', bg="white", font=('Arial', 12))
                label_nodos.place(x=10, y=50)

                label_profundidad = tk.Label(
                    reporte, text=f'Profundidad: {self.profundidadArbol}', fg='black', bg="white", font=('Arial', 12))
                label_profundidad.place(x=10, y=80)

                label_tiempo = tk.Label(
                    reporte, text=f'Tiempo de computo: {self.tiempo_computo} s', fg='black', bg="white", font=('Arial', 12))
                label_tiempo.place(x=10, y=110)

                label_costo = tk.Label(
                    reporte, text=f'Costo: {self.costo}', fg='black', bg="white", font=('Arial', 12))
                label_costo.place(x=10, y=150)
                self.stop_sound()
        # Botón para iniciar el algoritmo seleccionado
        boton_inicio = tk.Button(
            self, text="Iniciar algoritmo", command=lambda: (iniciar_algoritmo(), inhabilitarAlgoritmo()), bg="black", fg="white")
        boton_inicio.pack()
        boton_inicio.place(x=775, y=215)
        boton_inicio.config(font=('Times New Roman', 10))

        # Botón para seleccionar busqueda
        boton_seleccion = tk.Button(
            self, text="Seleccionar", command=lambda: (seleccionarBusqueda(), inhabilitarSeleccion()), bg="black", fg="white")
        boton_seleccion.pack()
        boton_seleccion.place(x=800, y=140)
        boton_seleccion.config(font=('Times New Roman', 10))

        # Botón de reinicio
        boton_reiniciar = tk.Button(
            self, text="Reiniciar", command=self.reiniciar_programa, bg="black", fg="white")
        boton_reiniciar.pack()
        boton_reiniciar.place(x=800, y=550)
        boton_reiniciar.config(font=('Times New Roman', 10))

        # Creditos
        def mostrar_creditos():
            ventana_creditos = tk.Toplevel(self)
            ventana_creditos.title("Créditos")
            ventana_creditos. geometry("300x200")
            ventana_creditos.config(bg="white")

            # Crear una etiqueta para mostrar los créditos del programa
            etiqueta_creditos = tk.Label(
                ventana_creditos, text="Créditos \n  \n Laura Daniela Jaimes - 2040430 \n Diana Marcela Cadena - 2041260 \n Mayra Alejandra Sanchez - 2040506")
            etiqueta_creditos.pack()
            etiqueta_creditos.config(font=('Times New Roman', 10), bg="white")
            etiqueta_creditos.place(x=50, y=50)

        boton_creditos = tk.Button(
            self, text="Créditos", command=mostrar_creditos, bg="black", fg="white")
        boton_creditos.pack()
        boton_creditos.config(font=('Times New Roman', 10))
        boton_creditos.place(x=700, y=550)

    def reiniciar_programa(self):
        self.destroy()  # Cierra la ventana actual
        Interfaz()  # Abre una nueva ventana
