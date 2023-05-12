import numpy as np
from algoritmos.Nodo_noInformada import Nodo

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
        0
        # print("encontró un cell sin semilla")

    # Caso donde encuentre un cell y tenga semilla
    if (matriz[yI, xI] == 4):
        # print("encontró un cell con semilla")
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


def profundidad(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []
    # matrizInicio = matriz_juego

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                # matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion del agente
                pos_esfera.append([j, i])  # x=j(columnas), y=i(filas)

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
    while len(pila) > 0:  # condicion de parada
        nodo = pila.pop()  # extraer el primero de la pila

        nodos_visitados.append(nodo.estadoAgente)
        nodos_expandidos += 1
        if (nodo.condicionGanar(pos_esfera)):
            # Retorno la solución
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
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad