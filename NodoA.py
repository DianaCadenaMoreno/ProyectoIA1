class Nodo:
    def __init__(self, matriz, posAgente, estado, recorrido, nodos_visitados, semillas, esferas, profundidad, num_esferas):
        self.matriz = matriz
        self.estado = estado
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados  # evitar devolverse
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.num_esferas = num_esferas

    def condicionGanar(self):
        # if(self.estado[0] == self.estado[1]):
        #     return True
        # if()
        # condicion de cero(llego a la meta) y condicion del agente sean igual los dos en true
        return self.estado[0] == self.estado[1]

    def marcar(self):
        # Encontramos las esferas
        if (self.esferas >= 1):
            self.estado[0] = True
            # self.nodos_visitados = []  # para que pueda devolverse

        if (self.esferas >= 2):  # Encontramos las esferas
            self.estado[1] = True
  
    

    # def condicionGanar(self):
    #     return self.estado[0] == True

    # def marcar(self):
    #     if (self.num_esferas == self.esferas):
    #         self.estado[0] = True
