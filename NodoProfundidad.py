class Nodo:
    def __init__(self, matriz, posAgente, estado, recorrido, visitados):
        """"
        matriz = Estado actual del juego
        posAgente = posicion actual del raton x,y (enteros)
        estado = estado de los objetivos queso,pelota (booleanos)
        """
        
        self.matriz = matriz
        self.x = posAgente[0]
        self.y = posAgente[1]
        self.queso = estado[0]
        self.pelota = estado[1]
        self.recorrido = recorrido
        self.visitados = visitados

    def verificar_perdi(self):
        return self.matriz[self.y,self.x] == 3
    
    def verificar_ganar(self):
        return self.pelota and self.queso 
    
    def marcar_objetivos(self):
        if not(self.queso) and self.matriz[self.y,self.x]==4:
            self.queso = True
            self.visitados = []

        if self.matriz[self.y,self.x]==5 and self.queso:
            self.pelota= True 

    def generar_hijos(self):
        #Hijo de arriba
        hijos = []
        x = self.x
        y = self.y-1
        
        if y >= 0 and not((x,y) in self.visitados) and self.matriz[y,x]!=2: #verificar que estoy en el tablero
            recorrido = self.recorrido.copy()
            recorrido.append((x,y))
            visitados = self.visitados.copy()
            visitados.append((x,y))
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.queso,self.pelota),
                recorrido,
                visitados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)

        #Hijo de abajo
        
        x = self.x
        y = self.y+1
        
        if y < self.matriz.shape[0] and not((x,y) in self.visitados) and self.matriz[y,x] !=2: #verificar que estoy en el tablero
            recorrido = self.recorrido.copy()
            recorrido.append((x,y))
            visitados = self.visitados.copy()
            visitados.append((x,y))
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.queso,self.pelota),
                recorrido,
                visitados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)

        #Hijo de la izquierda 
        
        x = self.x-1
        y = self.y
        
        if x >= 0 and not((x,y) in self.visitados) and self.matriz[y,x] !=2: #verificar que estoy en el tablero
            recorrido = self.recorrido.copy()
            recorrido.append((x,y))
            visitados = self.visitados.copy()
            visitados.append((x,y))
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.queso,self.pelota),
                recorrido,
                visitados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)

        #Hijo de la derecha
    
        x = self.x+1
        y = self.y
        
        if x < self.matriz.shape[1] and not((x,y) in self.visitados) and self.matriz[y,x] !=2: #verificar que estoy en el tablero
            recorrido = self.recorrido.copy()
            recorrido.append((x,y))
            visitados = self.visitados.copy()
            visitados.append((x,y))
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.queso,self.pelota),
                recorrido,
                visitados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)

        return hijos    