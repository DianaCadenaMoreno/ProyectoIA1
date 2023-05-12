from algoritmos.Nodo_Informada import Nodo

def verficarMovimientos(xI, yI, copiaEsferas, copiaEstadoAgente, copiaMatriz, copiaSemillas, copiaFn, matriz, copiaCostoAgente, heuristica, funcionHeuristica):
    esferas = copiaEsferas
    estadoAgente = copiaEstadoAgente
    matrizNew = copiaMatriz
    costo1 = 0
    costo2 = 0
    semillasRecolectadas = copiaSemillas
    fn = copiaFn
    Final = []
    heuristica = funcionHeuristica
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
        suma = costo2 + heuristica
        fn[0] = suma
        costoAgente[0] = costo2

    if (matriz[yI, xI] == 5):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        semillasRecolectadas[0] += 1
        suma = costo2 + heuristica
        fn[0] = suma
        costoAgente[0] = costo2
        if ([(xI, yI)] not in estadoAgente[3]):
            if (semillasRecolectadas[0] >= 1):
                estadoAgente[3] = [[xI, yI]]

    # Caso donde encuentre un cell y no tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 7
        costo2 = costo1 + costoAgente[-1]
        suma = costo2 + heuristica
        fn[0] = suma
        costoAgente[0] = costo2

    # Caso donde encuentre un cell y tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        semillasRecolectadas[0] -= 1
        suma = costo2 + heuristica
        fn[0] = suma
        costoAgente[0] = costo2

    # Caso donde encuentre un freezer y no tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 4
        costo2 = costo1 + costoAgente[-1]
        suma = costo2 + heuristica
        fn[0] = suma
        costoAgente[0] = costo2

    # Caso donde encuentre un freezer y tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente[-1]
        suma = costo2 + heuristica
        fn[0] = suma
        semillasRecolectadas[0] -= 1
        costoAgente[0] = costo2

    estadoAgente[0] = ((xI, yI))
    Final = matrizNew, estadoAgente, esferas, costoAgente, semillasRecolectadas, heuristica, fn
    return Final


def A_estrella(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []
    pos_semillas = []

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                break  # romper ciclo para eficiencia

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion del agente
                pos_esfera.append([j, i])  # x=j(columnas), y=i(filas)

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 5:  # posicion del agente
                pos_semillas.append([j, i])  # x=j(columnas), y=i(filas)

    semillas = [[] for _ in range(len(pos_semillas))]

    raiz = Nodo(
        matriz_juego,
        [pos_agente, [], [], semillas],
        [pos_agente],
        [[pos_agente], [], [], semillas],
        [0],
        [0, pos_esfera],
        0,
        [0],
        0,
        [0])

    cola = [raiz]
    nodos_visitados = []
    while len(cola) > 0:  # condicion de parada
        nodo = min(cola, key=lambda x: sum(x.fn))
        cola.remove(nodo)  # extrae el ultimo elemento de primero
        costoAgente = nodo.costo.copy()

        nodos_visitados.append(nodo.estadoAgente)
        nodos_expandidos += 1
        if (nodo.condicionGanar(pos_esfera)):
            # Retorno la solución
            costo = nodo.costo.pop()
            final = nodo.recorrido, nodos_expandidos, nodo.profundidad, costo, nodo.fn, matriz_juego
            return final

        x = nodo.estadoAgente[0][0]
        y = nodo.estadoAgente[0][1]
        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.fn.copy(), nodo.matriz, nodo.costo.copy(), nodo.heuristica, nodo.encontrar_heuristica())
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3],
                movimientos[5],
                movimientos[6]

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
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.fn.copy(), nodo.matriz, nodo.costo.copy(), nodo.heuristica, nodo.encontrar_heuristica())
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3],
                movimientos[5],
                movimientos[6]

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
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.fn.copy(), nodo.matriz, nodo.costo.copy(), nodo.heuristica, nodo.encontrar_heuristica())
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3],
                movimientos[5],
                movimientos[6]

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
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.fn.copy(), nodo.matriz, nodo.costo.copy(), nodo.heuristica, nodo.encontrar_heuristica())
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                movimientos[4],
                movimientos[2],
                nodo.profundidad + 1,
                movimientos[3],
                movimientos[5],
                movimientos[6]

            )
            nodos_creados += 1
            if (movimientos[1] not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad