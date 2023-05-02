class Nodo:
    def __init__(self, matriz, posAgente, estado,  recorrido, nodos_visitados):
        self.matriz = matriz
        self.posAgente = posAgente
        self.estado = estado
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados,
        # self.profundidad = profundidad  # evitar devolverse

    def condicionGanar(self):
        # condicion de cero(llego a la meta) y condicion del agente sean igual los dos en true
        print("el estado", self.estado)
        return self.estado[0] == self.estado[1]  # encontro a aida y al avion

    def marcar(self):
        # Encontramos las esferas
        # self.posAgente[1] representa las filas
        if self.matriz[self.posAgente[1], self.posAgente[0]] == 2 and (self.estado[0]) == False:
            # se encontró a aida, solo cuando encuentra a aida el se puede devolver
            self.estado[0] = True
            self.nodos_visitados = []  # para que pueda devolverse

        # Encontramos las esferas

        if self.estado[0] and self.matriz[self.posAgente[1], self.posAgente[0]] == 7:
            self.estado[1] = True  # Se econtró al avion

    def validarPerder(self):
        x, y = self.posAgente[1], self.posAgente[0]
        return self.matriz[x, y] == 4 or self.matriz[x, y] == 5 or self.matriz[x, y] == 6
