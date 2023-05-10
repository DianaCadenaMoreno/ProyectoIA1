import numpy as np
from Nodo import Nodo

juego = np.array([
    [0, 5, 3, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 3, 5, 1, 0, 2, 0],
    [0, 1, 1, 1, 3, 1, 1, 1, 1, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 4, 4, 0, 0, 1, 1, 5],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 5, 0, 0, 0],
    [1, 1, 1, 6, 1, 1, 0, 1, 1, 1]
])

# juego = np.array([
#     [1, 0, 6, 0],
#     [1, 2, 1, 0],
#     [1, 6, 1, 1],
#     [1, 1, 1, 0]
# ])
# esferas -> (2,0) y (1,2)


def ganar(estado, esferas):
    return (estado[1] == esferas)


def marcarEsfera(num, estado):
    if num == 1:
        estado[1][0] = True

    if num == 2:
        estado[1][1] = True


def amplitud(matriz_juego):
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
                # matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia
    print(pos_esfera)

    raiz = Nodo(
        matriz_juego,
        [pos_agente, [[], []]],
        [pos_agente],
        [[pos_agente], [[], []]],
        0,
        [0, pos_esfera],
        0,
        0)

    cola = [raiz]
    nodos_visitados = []
    while len(cola) > 0:  # condicion de parada
        # print("*", list(map(lambda nodo: nodo.recorrido, cola)), "*")
        nodo = cola.pop(0)  # extraer el primero de la cola
        # print("Nodos visitados", nodo.nodos_visitados)

        nodos_visitados.append(nodo.posAgente)

        nodos_expandidos += 1
        posEsfera = (0, 0)
        if (nodo.condicionGanar(pos_esfera)):
            # Retorno la solución
            # final = nodo.recorrido, nodos_creados, nodos_expandidos, nodo.profundidad, nodo.esferas, nodo.matriz
            final = nodo.recorrido, nodos_expandidos, nodo.profundidad, matriz_juego
            return final

        x = nodo.posAgente[0][0]
        y = nodo.posAgente[0][1]
        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and nodo.matriz[yI, xI] != 1:
            # pasar por valor
            # Hace el movimiento
            esferas = nodo.esferas.copy()
            estadoAgente = nodo.posAgente.copy()
            matrizNew = nodo.matriz.copy()
            print(nodo.matriz[yI, xI])
            print("agente", nodo.posAgente)
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0
                posEsfera = (yI, xI)
                if (estadoAgente[1][0] == []):
                    estadoAgente[1][0] = [xI, yI]
                    # print("a", estadoAgente[1][0])

                else:
                    estadoAgente[1][1] = [xI, yI]

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                matrizNew[yI, xI] = 0
                0
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia

            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,
                estadoAgente,
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            estadoAgente[0] = ((xI, yI))
            if (estadoAgente not in nodos_visitados):
                cola.append(hijo)
                recorrido.append((xI, yI))
                0
            print(nodos_visitados)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and nodo.matriz[yI, xI] != 1:
            # pasar por valor
            esferas = nodo.esferas.copy()
            estadoAgente = nodo.posAgente.copy()
            matrizNew = nodo.matriz.copy()
            print(nodo.matriz[yI, xI])
            print("agente", nodo.posAgente)
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0
                posEsfera = (yI, xI)
                if (estadoAgente[1][0] == []):
                    estadoAgente[1][0] = [xI, yI]
                    print("a", estadoAgente[1][0])

                else:
                    estadoAgente[1][1] = [xI, yI]

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                matrizNew[yI, xI] = 0
                0
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia

            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,
                estadoAgente,
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            estadoAgente[0] = ((xI, yI))
            if (estadoAgente not in nodos_visitados):
                # print("dentro", estadoAgente)
                # print("dentro2", nodos_visitados)
                cola.append(hijo)
                # nodos_visitados.append(hijo.posAgente)
                recorrido.append((xI, yI))
                0
                print(nodos_visitados)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and nodo.matriz[yI, xI] != 1:
            # pasar por valor
            esferas = nodo.esferas.copy()
            estadoAgente = nodo.posAgente.copy()
            matrizNew = nodo.matriz.copy()
            print(nodo.matriz[yI, xI])
            print("agente", nodo.posAgente)
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0
                posEsfera = (yI, xI)
                if (estadoAgente[1][0] == []):

                    estadoAgente[1][0] = [xI, yI]
                    print("a", estadoAgente[1][0])

                else:
                    estadoAgente[1][1] = [xI, yI]

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                matrizNew[yI, xI] = 0
                0
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia

            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,
                estadoAgente,
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            estadoAgente[0] = ((xI, yI))
            if (estadoAgente not in nodos_visitados):
                # print("dentro", estadoAgente)
                # print("dentro2", nodos_visitados)
                cola.append(hijo)
                # nodos_visitados.append(hijo.posAgente)
                recorrido.append((xI, yI))
                0
            print(nodos_visitados)

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and nodo.matriz[yI, xI] != 1:
            # pasar por valor
            esferas = nodo.esferas.copy()
            estadoAgente = nodo.posAgente.copy()
            matrizNew = nodo.matriz.copy()
            print(nodo.matriz[yI, xI])
            print("agente", nodo.posAgente)
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0
                posEsfera = (yI, xI)
                if (estadoAgente[1][0] == []):
                    estadoAgente[1][0] = [xI, yI]
                    print("a", estadoAgente[1][0])

                else:
                    estadoAgente[1][1] = [xI, yI]

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                matrizNew[yI, xI] = 0
                0
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia

            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,
                estadoAgente,
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.costo
            )
            nodos_creados += 1
            estadoAgente[0] = ((xI, yI))
            if (estadoAgente not in nodos_visitados):
                # print("dentro", estadoAgente)
                # print("dentro2", nodos_visitados)
                cola.append(hijo)
                # nodos_visitados.append(hijo.posAgente)
                recorrido.append((xI, yI))
                0
            print(nodos_visitados)

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad


# final = amplitud(juego)
# print(final[0])
print(amplitud(juego))
