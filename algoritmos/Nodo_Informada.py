class Nodo:
    def __init__(self, matriz, estadoAgente, recorrido, nodos_visitados, semillas, esferas, profundidad, costo, heuristica, fn):
        self.matriz = matriz
        self.estadoAgente = estadoAgente
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados
        self.semillas = semillas
        self.esferas = esferas
        self.profundidad = profundidad
        self.costo = costo
        self.heuristica = heuristica
        self.fn = fn

    # Funcion que verifica si el agente ya tiene todas las esferas y ha ganado
    # @param esferas (List)
    # @return Boolean

    def condicionGanar(self, esferas):
        return (self.estadoAgente[1] in esferas and self.estadoAgente[2] in esferas)

    # Esta función calcula la distancia de Manhattan entre dos puntos en un plano cartesiano (heurística de Avara)
    # @param estadoAgentex1, estadoAgentey1, posEsferax2, posEsferay2
    # @return distancia_manhattan(int)

    def distancia_manhattan(self, estadoAgentex1, estadoAgentey1, posEsferax2, posEsferay2):
        return abs(estadoAgentex1 - posEsferax2) + abs(estadoAgentey1 - posEsferay2)

    # Esta función encuentra una estimación de la distancia restante desde el estado actual del agente hasta el objetivo del problema, lo que permite guiar la búsqueda hacia una
    # solución de manera más eficiente.
    # @param
    # @return heuristica(int)

    def encontrar_heuristica(self):
        esferas = []
        for i in range(self.matriz.shape[0]):  # filas
            for j in range(self.matriz.shape[1]):  # columnas
                if self.matriz[i][j] == 6:  # posicion del agente
                    # x=j(columnas), y=i(filas)
                    esferas.append((j, i))

        distancias = []

        if len(esferas) == 0:
            return 0

        for esfera in esferas:
            distancias.append(self.distancia_manhattan(
                self.estadoAgente[0][0], self.estadoAgente[0][1], esfera[0], esfera[1]))

        if len(esferas) == 2:
            distancia_esferas = self.distancia_manhattan(
                esferas[0][0], esferas[0][1], esferas[1][0], esferas[1][1])
        else:
            distancia_esferas = 0

        if len(distancias) == 1:
            self.heuristica = distancia_esferas + distancias[0]
        else:
            self.heuristica = distancia_esferas + \
                min(distancias[0], distancias[1])
        return self.heuristica
