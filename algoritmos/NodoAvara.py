class Nodo:
    def __init__(self, matriz, posAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, estado, heuristica):
        self.matriz = matriz
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.estado = estado
        self.heuristica = heuristica

    def condicionGanar(self):
        if (self.estado[0] == True and self.estado[1] == True):
            return True

    def marcar(self):
        # Encontramos la primera esfera
        if self.esferas[0] == 1:
            self.estado[0] = True
            # para que pueda devolverse, despues de encontrar la primera esfera
            self.nodos_visitados = []

        # Encontramos la segunda esfera
        if self.esferas[0] == 2:
            self.estado[1] = True

    def encontrar_heuristica(self):
        # Para calcular la heurística, podemos estimar la distancia restante
        # desde el estado actual hasta el estado objetivo. Podemos usar la distancia
        # de Manhattan para estimar esta distancia.

        # Encontrar las posiciones de las esferas y el agente
        posiciones = []
        posiciones.posAgente.append(())
        # for i in range(len(self.matriz[0])):
        #     for j in range(len(self.matriz[1])):
        #         if self.matriz[i][j] == 2:
        #             posiciones.append((i, j))
        #         elif self.matriz[i][j] == 6:
        #             posiciones.append((i, j))

    
        return posiciones