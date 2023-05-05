class Nodo:
    def __init__(self, matriz, posAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, estado):
        self.matriz = matriz
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.estado = estado

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