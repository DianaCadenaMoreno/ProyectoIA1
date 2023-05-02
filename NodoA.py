class Nodo:
    def __init__(self, matriz, posAgente, estado, recorrido, nodos_visitados, semillas, esferas, profundidad):
        self.matriz = matriz
        self.estado = estado
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.eferas = esferas
        self.profundidad = profundidad

    def condicionGanar(self):
        # condicion de cero(llego a la meta) y condicion del agente sean igual los dos en true
        return self.estado[0] == self.estado[1]

    def marcar(self):
        # Encontramos las esferas
        if (self.eferas >= 1):
            self.estado[0] = True
            # self.nodos_visitados = []  # para que pueda devolverse

        if (self.eferas >= 2):  # Encontramos las esferas
            self.estado[1] = True
