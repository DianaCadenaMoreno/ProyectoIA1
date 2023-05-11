import numpy as np
from algoritmos.Nodo_noInformada import Nodo

# juego = np.array([
#     [1, 6, 5, 5],
#     [4, 2, 1, 0],
#     [4, 1, 1, 0],
#     [0, 6, 4, 0]
# ])

juego = np.array([
    [1, 1, 1, 6, 2, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 4, 1, 1, 1, 5],
    [1, 6, 1, 1, 1, 1]
])

# juego = np.array([
#     [5, 2, 4, 0, 0],
#     [1, 1, 1, 5, 0],
#     [1, 0, 6, 4, 0],
#     [1, 1, 1, 1, 0],
#     [1, 1, 6, 0, 5]
# ])

# juego = np.array([
#     [1, 2, 0, 0, 0],
#     [1, 5, 1, 1, 0],
#     [1, 0, 6, 4, 0],
#     [1, 1, 1, 1, 0],
#     [1, 1, 6, 0, 5]
# ])

# juego = np.array([
#     [0, 5, 3, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
#     [0, 1, 1, 0, 3, 5, 1, 0, 2, 0],
#     [0, 1, 1, 1, 3, 1, 1, 1, 1, 0],
#     [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 4, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 0, 4, 4, 0, 0, 1, 1, 5],
#     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
#     [0, 0, 0, 0, 1, 1, 5, 0, 0, 0],
#     [1, 1, 1, 6, 1, 1, 0, 1, 1, 1]
# ])

# juego = np.array([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 0, 3, 5, 1, 0, 1, 6],
#     [0, 1, 1, 1, 3, 1, 1, 1, 1, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 1, 4, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 0, 4, 1, 0, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#     [6, 0, 0, 0, 0, 0, 0, 0, 4, 0]
# ])

# juego = np.array([
#     [0, 5, 3, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
#     [0, 1, 1, 0, 3, 5, 1, 0, 2, 0],
#     [0, 1, 1, 1, 3, 1, 1, 1, 1, 0],
#     [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 4, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 0, 4, 4, 0, 0, 1, 1, 5],
#     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
#     [0, 0, 0, 0, 1, 1, 5, 0, 0, 0],
#     [1, 1, 1, 6, 1, 1, 0, 1, 1, 1]
# ])
# esferas -> (2,0) y (1,2)


def verficarMovimientos(xI, yI, copiaEsferas, copiaEstadoAgente, copiaMatriz, copiaSemillas, copiaCostoAgente, matriz, pos_semillas):
    # estadoAgente[3] = [0] * len(pos_semillas)
    esferas = copiaEsferas
    estadoAgente = copiaEstadoAgente
    print("Estado agente antes de entrar", estadoAgente)
    matrizNew = copiaMatriz
    costo1 = 0
    costo2 = 0
    semillasRecolectadas = copiaSemillas
    Final = []
    costoAgente = copiaCostoAgente

    if (matriz[yI, xI] == 0):
        costo1 += 1
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)

    if (matriz[yI, xI] == 6):
        esferas[0] += 1
        matrizNew[yI, xI] = 0
        if (esferas[0] == 1):
            estadoAgente[1] = [xI, yI]
        if (esferas[0] == 2):
            estadoAgente[2] = [xI, yI]
        costo1 += 1
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)

    if (matriz[yI, xI] == 5):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)
        semillasRecolectadas[0] += 1
        print("Semillas recolectadas:", semillasRecolectadas[0])
        # if (semillasRecolectadas[0] == 1):
        #     estadoAgente[3][0] = [(xI, yI)]
        # if (semillasRecolectadas[0] == 2):
        #     estadoAgente[3][1] = [(xI, yI)]
        if ([(xI, yI)] not in estadoAgente[3]):
            if (semillasRecolectadas[0] >= 1):
                estadoAgente[3] = [[xI, yI]]
                print(" ")
                print("ESTADO DEL AGENTE DESPUES DE COLOCAR LA SEMILLA",
                      estadoAgente[3])

    # Caso donde encuentre un cell y no tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 7
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)

    # Caso donde encuentre un cell y tenga semilla
    if (matriz[yI, xI] == 4 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)
        semillasRecolectadas[0] - 1
        # estadoAgente[3].pop()

    # Caso donde encuentre un freezer y no tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] == 0):
        matrizNew[yI, xI] = 0
        costo1 += 4
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)

    # Caso donde encuentre un freezer y tenga semilla
    if (matriz[yI, xI] == 3 and semillasRecolectadas[0] >= 1):
        matrizNew[yI, xI] = 0
        costo1 += 1
        costo2 = costo1 + costoAgente.pop()
        costoAgente.append(costo2)
        semillasRecolectadas[0] - 1
        # estadoAgente[3].pop()

    estadoAgente[0] = ((xI, yI))
    Final = matrizNew, estadoAgente, esferas, costoAgente, semillasRecolectadas
    return Final


def costo_uniforme(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []
    pos_semillas = []
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
                # matriz_juego[i][j] = 0  # actualizar

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 5:  # posicion del agente
                pos_semillas.append([j, i])  # x=j(columnas), y=i(filas)
                # matriz_juego[i][j] = 0  # actualizar

    print("Posiciones ideales", pos_esfera)
    print("Semillas a recolectar", pos_semillas)
    print("Listas",  [[] for _ in range(len(pos_semillas))])
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
    while len(cola) > 0:  # condicion de parada
        # print("*", list(map(lambda nodo: nodo.recorrido, cola)), "*")
        nodo = min(cola, key=lambda x: sum(x.costo))
        cola.remove(nodo)  # extrae el ultimo elemento de primero
        costoAgente = nodo.costo.copy()

        nodos_visitados.append(nodo.estadoAgente)
        nodos_expandidos += 1
        if (nodo.condicionGanar(pos_esfera)):
            # Retorno la solución
            # final = nodo.recorrido, nodos_creados, nodos_expandidos, nodo.profundidad, nodo.esferas, nodo.matriz
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

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            print("nodos_visitados", nodos_visitados)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            print("nodos_visitados", nodos_visitados)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            print("nodos_visitados", nodos_visitados)
        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and nodo.matriz[yI, xI] != 1:
            movimientos = verficarMovimientos(xI, yI, nodo.esferas.copy(
            ), nodo.estadoAgente.copy(), nodo.matriz.copy(), nodo.semillas.copy(), nodo.costo.copy(), nodo.matriz, pos_semillas)
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            # estado = nodo.estadoEsferas.copy()
            hijo = Nodo(
                movimientos[0],
                movimientos[1],
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
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
            print("nodos_visitados", nodos_visitados)

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad


# final = amplitud(juego)
# print(final[0])
print(costo_uniforme(juego))
