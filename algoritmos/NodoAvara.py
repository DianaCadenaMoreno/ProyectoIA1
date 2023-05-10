class Nodo:
    def __init__(self, matriz, posAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, estadoEsferas, costo, heuristica):
        self.matriz = matriz
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.estadoEsferas = estadoEsferas
        self.costo = costo
        self.heuristica = heuristica

    def condicionGanar(self):
        if (self.estadoEsferas[0] == True and self.estadoEsferas[1] == True):
            return True

    def econtrarEsfera(self):
        # Encontramos la primera esfera
        if self.esferas[0] == 1:
            self.estadoEsferas[0] = True
            # para que pueda devolverse, despues de encontrar la primera esfera
            # self.nodos_visitados = []

        # Encontramos la segunda esfera
        if self.esferas[0] == 2:
            self.estadoEsferas[1] = True
        
    # calcula la distancia de Manhattan entre dos puntos en un plano cartesiano (heurística de Avara)
    def distancia_manhattan(self,posAgentex1,posAgentey1,posEsferax2,posEsferay2):
        return abs(posAgentex1 - posEsferax2) + abs(posAgentey1 - posEsferay2)

    def encontrar_heuristica(self):

        esferas =[]
        for i in range(self.matriz.shape[0]):  # filas
            for j in range(self.matriz.shape[1]):  # columnas
                if self.matriz[i][j] == 6:  # posicion del agente
                    # x=j(columnas), y=i(filas)
                    esferas.append((j,i))              
                    break  # romper ciclo para eficiencia
        
        distancias=[]

        if len(esferas) == 0:
            return 0
        
        for esfera in esferas:
            print(f"Posiciones: {self.posAgente[0]}, {self.posAgente[1]}, {esfera[0]}, {esfera[1]}")
            distancias.append(self.distancia_manhattan(self.posAgente[0], self.posAgente[1], esfera[0], esfera[1]))

        if len(esferas) == 2:
            distancia_esferas = self.distancia_manhattan(esferas[0][0], esferas[0][1], esferas[1][0], esferas[1][1])
        else:
            distancia_esferas = 0

        if len(distancias) == 1:
            self.heuristica = distancia_esferas + distancias[0]
        else:
            self.heuristica = distancia_esferas + min(distancias[0], distancias[1])
        print("heuristica",self.heuristica)
        return self.heuristica 
    
    

            

    