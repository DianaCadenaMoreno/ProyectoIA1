class Nodo:
    def __init__(self, matriz, estadoAgente, recorrido, nodos_visitados, semillas, esferas, profundidad,  costo):
        self.matriz = matriz
        self.estadoAgente = estadoAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.costo = costo

    def condicionGanar(self, esferas):
        return (self.estadoAgente[1] in esferas and self.estadoAgente[2] in esferas)
