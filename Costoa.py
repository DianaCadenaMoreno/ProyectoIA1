import numpy as np
from NodoC import Nodo
import queue


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

# posicion esfera 1 -> (0,4)
# posicion esfera 2 -> (3,9)

# juego = np.array([
#     [0, 6],
#     [0, 1],
#     [0, 2],
# ])

juego = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 2],
    [0, 1, 6, 1],
    [5, 0, 0, 0]
])


def amplitud(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    num_esferas = 0

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion del agente
                num_esferas += 1  # x=j(columnas), y=i(filas)
                print("num_esferas", num_esferas)
                break  # romper ciclo para eficiencia

    costos = [0]

    raiz = Nodo(
        matriz_juego,
        pos_agente,
        [pos_agente],
        [pos_agente],
        0,
        [0],
        0,
        num_esferas,
        costos)

    cola = queue.PriorityQueue()
    cola.put((costos, raiz))

    while not cola.empty():  # condicion de parada
        # print("*", list(map(lambda nodo: nodo.recorrido, cola)), "*")
        nodo = cola.get()[1]  # extraer el primero de la cola
        nodos_expandidos += 1

        if (nodo.condicionGanar()):
            # Retorno la solución
            final = nodo.recorrido, nodos_creados, nodos_expandidos, nodo.profundidad, nodo.esferas, nodo.num_esferas
            return final

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            esferas = nodo.esferas.copy()
            costoAgente = nodo.costo.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()

            # matrizJuegoNew = nodo.matriz.copy()
            # matrizJuegoNew[xI, yI] = 2
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                costo1 += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                semillasRecolectadas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                semillasRecolectadas - 1

            nodos_visitados.append((xI, yI))
            recorrido.append((xI, yI))

            hijo = Nodo(
                nodo.matriz,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                nodo.num_esferas,
                costoAgente
            )
            nodos_creados += 1
            # hijo.marcar()  # Evaluar que sucede en la posicion
            # hijo.marcar()  # Evaluar que sucede en la posicion
            cola.put(hijo)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            esferas = nodo.esferas.copy()
            costoAgente = nodo.costo.copy()
            costo1 = 0
            costo2 = 0
            semillasRecolectadas = nodo.semillas.copy()
            nodos_visitados = nodo.nodos_visitados.copy()
            recorrido = nodo.recorrido.copy()

            # matrizJuegoNew = nodo.matriz.copy()
            # matrizJuegoNew[xI, yI] = 2
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                costo1 += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)

            if (nodo.matriz[yI, xI] == 5):
                costo1 += 1
                costoAgente.append(costo2)
                semillasRecolectadas[0] += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                costo1 += 7
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                costo += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                semillasRecolectadas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                costo1 += 4
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                # print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                # print("encontró un freezer con semilla")
                costo1 += 1
                costo2 = costo1 + costoAgente.pop(0)
                costoAgente.append(costo2)
                semillasRecolectadas - 1

            nodos_visitados.append((xI, yI))
            recorrido.append((xI, yI))

            hijo = Nodo(
                nodo.matriz,
                (xI, yI),
                recorrido,
                nodos_visitados,
                semillasRecolectadas,
                esferas,
                nodo.profundidad + 1,
                nodo.num_esferas,
                costoAgente
            )
            nodos_creados += 1
            # hijo.marcar()  # Evaluar que sucede en la posicion
            # hijo.marcar()  # Evaluar que sucede en la posicion
            cola.put(hijo)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            esferas = nodo.esferas.copy()
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                print("encontró un cell con semilla")
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                print("encontró un freezer con semilla")
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.num_esferas
            )
            nodos_creados += 1
            # hijo.marcar()  # Evaluar que sucede en la posicion
            cola.put(hijo)

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            esferas = nodo.esferas.copy()
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                print("encontró un cell con semilla")
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                print("encontró un freezer sin semilla")

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                print("encontró un freezer con semilla")
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                nodo.num_esferas
            )
            nodos_creados += 1
            # hijo.marcar()  # Evaluar que sucede en la posicion
            cola.put(hijo)

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad


# final = amplitud(juego)
# print(final[0])
print(amplitud(juego))
