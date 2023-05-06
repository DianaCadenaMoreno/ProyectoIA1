class Nodo:
    def __init__(self, matriz, posAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, estadoEsferas, costo):
        self.matriz = matriz
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.estadoEsferas = estadoEsferas
        self.costo = costo

    def condicionGanar(self):
        if (self.posAgente[1][0] == True and self.posAgente[1][1] == True):
            return True

    def econtrarEsfera(self):
        # Encontramos la primera esfera
        if self.esferas[0] == 1:
            # print("aaaaaaaa", self.posAgente[1][0])
            self.posAgente[1][0] = True
            # para que pueda devolverse, despues de encontrar la primera esfera
            # self.nodos_visitados = []

        # Encontramos la segunda esfera
        if self.esferas[0] == 2:
            self.posAgente[1][1] = True
