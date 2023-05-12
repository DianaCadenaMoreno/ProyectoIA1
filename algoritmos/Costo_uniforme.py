from algoritmos.Nodo_noInformada import Nodo

# Esta funcion realiza las acciones que puede hacer el agente, si pasa por una esfera, una semilla, un enemigo sin semilla o un enemigo con semilla
# @param xI (int), yI (int), copiaEsferas(list), copiaEstadoAgente(list), copiaMatriz(NumPy array), matriz(NumPy array)
# @return la lista matrizNew, estadoAgente, esferas, costoAgentey semillasRecolectadas (List)


def verficarMovimientos(xI, yI, copiaEsferas, copiaEstadoAgente, copiaMatriz, copiaSemillas, copiaCostoAgente, matriz, pos_semillas):
    esferas = copiaEsferas
    estadoAgente = copiaEstadoAgente
    matrizNew = copiaMatriz
    costo1 = 0
    costo2 = 0
    semillasRecolectadas = copiaSemillas
    Final = []
    costoAgente = copiaCostoAgente

    if (matriz[yI, xI] == 0):
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2

    if (matriz[yI, xI] == 6):
        esferas[0] += 1
        matrizNew[yI, xI] = 0
        if (esferas[0] == 1):
            estadoAgente[1] = [xI, yI]
        if (esferas[0] == 2):
            estadoAgente[2] = [xI, yI]
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2

    if (matriz[yI, xI] == 5):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2
        semillasRecolectadas[0] += 1
        if ([(xI, yI)] not in estadoAgente[3]):
            if (semillasRecolectadas[0] >= 1):
                estadoAgente[3] = [[xI, yI]]

    # Caso donde encuentre un cell y no tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 7
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2

    # Caso donde encuentre un cell y tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2
        semillasRecolectadas[0] -= 1

    # Caso donde encuentre un freezer y no tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 4
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2

    # Caso donde encuentre un freezer y tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        costoAgente[0] = costo2
        semillasRecolectadas[0] -= 1

    estadoAgente[0] = ((xI, yI))
    Final = matrizNew, estadoAgente, esferas, costoAgente, semillasRecolectadas
    return Final

# Realiza el algoritmo de busqueda por costo uniforme
# @param matriz_juego(NumPy array)
# @return nodo.recorrido (List), nodos_expandidos(int),nodo.profundidad(int), costo(int), matriz_juego(NumPy array)


def costo_uniforme(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []
    pos_semillas = []

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)
                break

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion de las esferas
                pos_esfera.append([j, i])

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 5:  # posicion de las semillas
                pos_semillas.append([j, i])

    semillas = [[] for _ in range(len(pos_semillas))]

    raiz = Nodo(
        matriz_juego,
        [pos_agente, [], [], semillas],
        [pos_agente],
        [[pos_agente], [], [], semillas],
        [0],
        [0, pos_esfera],
        0,
        [0])

    cola = [raiz]
    nodos_visitados = []
    while len(cola) > 0:
        nodo = min(cola, key=lambda x: sum(x.costo))
        cola.remove(nodo)
        costoAgente = nodo.costo.copy()

        nodos_visitados.append(nodo.estadoAgente)
        nodos_expandidos += 1
        if (nodo.condicionGanar(pos_esfera)):
            costo = nodo.costo.pop()
            final = nodo.recorrido, nodos_expandidos, nodo.profundidad, costo, matriz_juego
            return final

        x = nodo.estadoAgente[0][0]
        y = nodo.estadoAgente[0][1]
        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)

            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3]
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()

            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3]
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3]
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0
        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3]
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0

    return "No hay solucion", nodo.recorrido, nodos_expandidos, nodo.profundidad, costo, matriz_juego
