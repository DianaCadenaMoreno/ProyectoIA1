from algoritmos.Nodo_noInformada import Nodo

# Esta funcion realiza las acciones que puede hacer el agente, si pasa por una esfera, una semilla, un enemigo sin semilla o un enemigo con semilla
# @param xI (int), yI (int), copiaEsferas(list), copiaEstadoAgente(list), copiaMatriz(NumPy array), matriz(NumPy array)
# @return la lista con la matriz actualizada, el estado del agente y las esferas (List)


def verficarMovimientos(xI, yI, copiaEsferas, copiaEstadoAgente, copiaMatriz, matriz):
    esferas = copiaEsferas
    estadoAgente = copiaEstadoAgente
    matrizNew = copiaMatriz
    Final = []

    if (matriz[yI, xI] == 6):
        esferas[0] += 1
        matrizNew[yI, xI] = 0
        if (esferas[0] == 1):
            estadoAgente[1] = [xI, yI]
        if (esferas[0] == 2):
            estadoAgente[2] = [xI, yI]

    if (matriz[yI, xI] == 5):
        matrizNew[yI, xI] = 0

    # Caso donde encuentre un cell y no tenga semilla
    if (matriz[yI, xI] == 4):
        matrizNew[yI, xI] = 0

    # Caso donde encuentre un cell y tenga semilla
    if (matriz[yI, xI] == 4):
        matrizNew[yI, xI] = 0

    # Caso donde encuentre un freezer y no tenga semilla
    if (matriz[yI, xI] == 3):
        matrizNew[yI, xI] = 0
        0

    # Caso donde encuentre un freezer y tenga semilla
    if (matriz[yI, xI] == 3):
        matrizNew[yI, xI] = 0

    estadoAgente[0] = ((xI, yI))
    Final = matrizNew, estadoAgente, esferas
    return Final

# Realiza el algoritmo de busqueda por profundidad
# @param matriz_juego (NumPy array)
# @return nodo.recorrido (List), nodos_expandidos(int),nodo.profundidad(int), matriz_juego(NumPy array)


def profundidad(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)
                break  # romper ciclo para eficiencia

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion de las esferas
                pos_esfera.append([j, i])

    raiz = Nodo(
        matriz_juego,
        [pos_agente, [], []],
        [pos_agente],
        [[pos_agente], [], []],
        0,
        [0, pos_esfera],
        0,
        0)

    pila = [raiz]
    nodos_visitados = []
    while len(pila) > 0:
        nodo = pila.pop()
        nodos_visitados.append(nodo.estadoAgente)
        nodos_expandidos += 1
        if (nodo.condicionGanar(pos_esfera)):

            final = nodo.recorrido, nodos_expandidos, nodo.profundidad, matriz_juego
            return final

        x = nodo.estadoAgente[0][0]
        y = nodo.estadoAgente[0][1]

        # genero los hijos

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.matriz)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                nodo.semillas,
                movimientos[2],
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                pila.append(hijo)
                recorrido.append((xI, yI))
                0

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.matriz)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                nodo.semillas,
                movimientos[2],
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                pila.append(hijo)
                recorrido.append((xI, yI))
                0

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.matriz)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                nodo.semillas,
                movimientos[2],
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                pila.append(hijo)
                recorrido.append((xI, yI))
                0

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.matriz)
            recorrido = nodo.recorrido.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,
                nodos_visitados,
                nodo.semillas,
                movimientos[2],
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                pila.append(hijo)
                recorrido.append((xI, yI))
                0

    return "No hay solucion", nodo.recorrido, nodos_expandidos, nodo.profundidad, matriz_juego
