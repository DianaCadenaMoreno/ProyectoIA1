import numpy as np
from NodoPeye import Nodo

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

# [(8, 2), (7, 2), (7, 1), (6, 1), (5, 1), (5, 2), (4, 2), (3, 2), (3, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 8), (3, 9)]

# posicion esfera 1 -> (0,4)
# posicion esfera 2 -> (3,9)

# juego = np.array([
#     [0, 6],
#     [0, 1],
#     [0, 2],
# ])

# Recorrido correcto [(1, 2), (0, 2), (0, 1), (0, 0), (1, 0)]

# juego = np.array([
#     [0, 0, 0, 0],
#     [0, 1, 1, 2],
#     [0, 1, 6, 1],
#     [5, 0, 0, 0]
# ])
# Recorrido correcto [(3, 1), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2)]

# juego = np.array([
#     [0, 0, 4, 1, 1],
#     [0, 1, 5, 0, 1],
#     [0, 1, 1, 0, 2],
#     [0, 1, 1, 1, 3],
#     [6, 0, 0, 0, 0]
# ])

juego = np.array([
    [0, 0, 1, 1, 1, 1],
    [3, 0, 0, 0, 0, 2],
    [0, 1, 1, 1, 1, 1],
    [6, 1, 1, 0, 0, 1],
    [0, 0, 4, 4, 0, 1],
    [1, 0, 5, 1, 6, 1]
])
# ajaaaaaaaa

# juego = np.array([
#     [1, 1, 1, 0, 0],
#     [1, 2, 6, 0, 0],
#     [1, 6, 1, 0, 0],
#     [1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0]
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

#     [1, 0, 6, 0],
#     [1, 2, 1, 0],
#     [1, 6, 1, 1],
#     [1, 1, 1, 0]
# ])


def costo_uniforme(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia

    raiz = Nodo(
        matriz_juego,
        pos_agente,
        [pos_agente],
        [pos_agente],
        [0],
        [0],
        0,
        [False, False],
        [0])

    cola = [raiz]

    while len(cola) > 0:  # condicion de parada
        # print("*", list(map(lambda nodo: nodo.recorrido, cola)), "*")
        nodo = min(cola, key=lambda x: sum(x.costo))
        cola.remove(nodo)  # extrae el ultimo elemento de primero
        costoAgente = nodo.costo.copy()
        # print(list(map(lambda nodo: nodo.recorrido, cola)))
        # print("costosAa", list(map(lambda nodo: nodo.costo, cola)))
        nodos_expandidos += 1
        if (nodo.condicionGanar()):
            # Retorno la solución
            final = "PARTE FINAL", nodo.recorrido, nodos_expandidos, nodo.profundidad, matriz_juego
            return final

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[yI, xI] != 1:
            esferas = nodo.esferas.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()

            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                estado
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costo2 = costo1 + costoAgente.pop()
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            hijo = Nodo(
                matrizNew,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                estado,
                costoAgente
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            if nodo.profundidad < 64:
                cola.append(hijo)
                nodos_visitados.append((xI, yI))
                recorrido.append((xI, yI))

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[yI, xI] != 1:
            esferas = nodo.esferas.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()

            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                estado
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costo2 = costo1 + costoAgente.pop()
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            hijo = Nodo(
                matrizNew,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                estado,
                costoAgente
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            if nodo.profundidad < 64:
                cola.append(hijo)
                nodos_visitados.append((xI, yI))
                recorrido.append((xI, yI))

            # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[yI, xI] != 1:
            esferas = nodo.esferas.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()

            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                estado
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costo2 = costo1 + costoAgente.pop()
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            hijo = Nodo(
                matrizNew,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                estado,
                costoAgente
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            if nodo.profundidad < 64:
                cola.append(hijo)
                nodos_visitados.append((xI, yI))
                recorrido.append((xI, yI))

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[yI, xI] != 1:
            esferas = nodo.esferas.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()

            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                estado
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costo2 = costo1 + costoAgente.pop()
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente[-1]
                costoAgente.append(costo2)
                semillasRecolectadas[0] - 1

            hijo = Nodo(
                matrizNew,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                estado,
                costoAgente
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            if nodo.profundidad < 64:
                cola.append(hijo)
                nodos_visitados.append((xI, yI))
                recorrido.append((xI, yI))

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad


# final = profundidad(juego)
# print(final[0])
print(costo_uniforme(juego))
