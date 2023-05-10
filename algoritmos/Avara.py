import numpy as np
from NodoAvara import Nodo

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

juego = np.array([
    [0, 5, 3, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 3, 5, 1, 0, 2, 0],
    [0, 1, 1, 1, 3, 1, 1, 1, 1, 6],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 4, 4, 0, 0, 1, 1, 5],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 5, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
])

# juego = np.array([
#     [0, 0, 6, 0],
#     [0, 2, 1, 6],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0]
# ])

def avara(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    num_esferas = 0
    # matrizInicio = matriz_juego
    esferas =[]

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 2:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                # matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia

    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 6:  # posicion del agente
                num_esferas += 1  # x=j(columnas), y=i(filas)
                esferas.append((j,i))
                # print("num_esferas", num_esferas)
                # print(esferas)               
                break  # romper ciclo para eficiencia
    
    # calcula la distancia de Manhattan entre dos puntos en un plano cartesiano (heurística de Avara)
    # def distancia_manhattan(x1,y1,x2,y2):
    #     return abs(x1 - x2) + abs(y1 - y2)

    # def heuristica(posicion):
    #     distancias=[]

    #     if len(esferas) == 0:
    #         return 0
        
    #     for esfera in esferas:
    #         distancias.append(distancia_manhattan(posicion[0], posicion[1], esfera[0], esfera[1]))

    #     if len(esferas) == 2:
    #         distancia_esferas = distancia_manhattan(esferas[0][0], esferas[0][1], esferas[1][0], esferas[1][1])
    #     else:
    #         distancia_esferas = 0

    #     if len(distancias) == 1:
    #         heuristica = distancia_esferas + distancias[0]
    #     else:
    #         heuristica = distancia_esferas + min(distancias[0], distancias[1])
        
    #     return heuristica
    # print(heuristica(pos_agente))

    raiz = Nodo(
        matriz_juego, #matriz
        pos_agente, #posAgente
        [pos_agente], #recorrido
        [pos_agente], #nodos_visitados
        0, #semillas
        [0], #esferas
        0, #profundidad
        [False, False], #estadoEsferas
        0, #costo
        0) #heuristica

    cola = [raiz]

    while len(cola) > 0:  # condicion de parada
       
        nodo = min(cola, key=lambda x: x.heuristica)
        cola.remove(nodo)  # extrae el ultimo elemento de primero
        
        # nodo = cola.pop(0)  # extraer el primero de la cola
        nodos_expandidos += 1
        # print(nodo.encontrar_heuristica())
        
        if (nodo.condicionGanar()):
            return nodo.recorrido, nodos_expandidos, nodo.profundidad, nodo.heuristica

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))  # Hace el movimiento
            esferas = nodo.esferas.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()
            nodo.heuristica = nodo.encontrar_heuristica()
                                            
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                # matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0
                # print("encontró un cell sin semilla")

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                # print("encontró un cell con semilla")
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                estado,
                nodo.costo,
                nodo.heuristica
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            cola.append(hijo)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            esferas = nodo.esferas.copy()
            estado = nodo.estadoEsferas.copy()
            nodo.heuristica = nodo.encontrar_heuristica()
            
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):

                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                estado,
                nodo.costo,
                nodo.heuristica
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            cola.append(hijo)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            esferas = nodo.esferas.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()
            nodo.heuristica = nodo.encontrar_heuristica()
            # print(nodo.encontrar_heuristica())

            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                estado,
                nodo.costo,
                nodo.heuristica
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            cola.append(hijo)

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            esferas = nodo.esferas.copy()
            estado = nodo.estadoEsferas.copy()
            matrizNew = nodo.matriz.copy()
            nodo.heuristica = nodo.encontrar_heuristica()
            
            if (nodo.matriz[yI, xI] == 6):
                esferas[0] += 1
                matrizNew[yI, xI] = 0

            if (nodo.matriz[yI, xI] == 5):
                nodo.semillas += 1
                matrizNew[yI, xI] = 0

            # Caso donde encuentre un cell y no tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0

            # Caso donde encuentre un cell y tenga semilla
            if (nodo.matriz[yI, xI] == 4):
                0
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            # Caso donde encuentre un freezer y no tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0

            # Caso donde encuentre un freezer y tenga semilla
            if (nodo.matriz[yI, xI] == 3):
                0
                matrizNew[yI, xI] = 0
                nodo.semillas - 1

            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            # estado = nodo.estadoEsferas.copy()

            hijo = Nodo(
                matrizNew,  # Compartido
                (xI, yI),
                recorrido,  # Nuevo
                nodos_visitados,  # Nuevo
                nodo.semillas,
                esferas,
                nodo.profundidad + 1,
                estado,
                nodo.costo,
                nodo.heuristica
            )
            nodos_creados += 1
            hijo.econtrarEsfera()
            cola.append(hijo)
            

    return "No hay solucion", nodos_creados, nodos_expandidos, nodo.profundidad

print(avara(juego))