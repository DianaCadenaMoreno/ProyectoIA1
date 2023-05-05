class Nodo:
    def __init__(self, matriz, posAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, num_esferas):
        self.matriz = matriz
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.num_esferas = num_esferas

    def condicionGanar(self):
        return self.num_esferas == self.esferas[0]