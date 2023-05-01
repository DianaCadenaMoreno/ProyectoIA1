class Nodo:
    def __init__(self, matriz, estado, posAgente, recorrido, nodos_visitados):
        self.matriz = matriz
        self.estado = estado
        self.posAgente = posAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados #evitar devolverse
    
    def condicionGanar(self):
        return self.estado[0] and self.estado[1] #condicion de cero(llego a la meta) y condicion del agente sean igual los dos en true    
    
    def marcar(self):
        if self.matriz[self.posAgente[1],self.posAgente[0]]==6 and not (self.estado[0]): #Encontramos las esferas
            self.estado[0] = True 
            self.nodos_visitados = [] #para que pueda devolverse

        # if self.matriz[self.posAgente[1],self.posAgente[0]]==5 and not (self.estado[0]): #Encontramos las esferas
        #     self.estado[1] = True 
