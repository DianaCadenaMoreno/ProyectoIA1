import numpy as np
from NodoProfe import Nodo

juego = np.array([
    [0, 1, 0, 0, 0, 7],
    [3, 0, 3, 0, 4, 0],
    [3, 6, 0, 0, 0, 3],
    [5, 0, 0, 4, 0, 0],
    [3, 3, 3, 0, 2, 0],
    [3, 3, 4, 4, 0, 1]

])


def amplitud(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    # Esto es para encontrar el agente
    for i in range(matriz_juego.shape[0]):  # filas
        for j in range(matriz_juego.shape[1]):  # columnas
            if matriz_juego[i][j] == 1:  # posicion del agente
                pos_agente = (j, i)  # x=j(columnas), y=i(filas)
                matriz_juego[i][j] = 0  # actualizar
                break  # romper ciclo para eficiencia
    raiz = Nodo(
        matriz_juego,
        pos_agente,
        # condición de meta es igual al false porque no ha encontrado esferas
        [True, False],
        [pos_agente],  # Recorrido
        [pos_agente]  # visitados
    )

    cola = [raiz]

    while len(cola) > 0:  # condicion de parada
        nodo = cola.pop(0)  # extraer el primero de la cola
        nodos_expandidos += 1
        print("Inicio")
        if (nodo.condicionGanar()):
            print(nodo.condicionGanar())
            print("Entre al primer if")
            return nodo.recorrido, nodos_creados, nodos_expandidos  # Retorno la solución

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 3:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            # para pasar una matriz de una posicion a otra, hacemos copia para no pasar la misma
            # Hace la accion de moverse para arriba
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar paso por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()
            print("Entre a arriba")
            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posicion
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodos_creados += 1  # cuando se crea el hijo es que se crea el nodo
            hijo.marcar()  # Evaluar que sucede en la posicion, si encontro a aida va cambiando el estado
            if not (hijo.validarPerder()):  # Esto es cuando esta dentro de los enemigos
                cola.append(hijo)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 3:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()
            print("Entre a abajo")
            hijo = Nodo(
                nodo.matriz,
                (xI, yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posicion
            if not (hijo.validarPerder()):  # Esto es cuando esta dentro de los enemigos
                cola.append(hijo)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 3:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()
            print("Entre a izquieerda")
            hijo = Nodo(
                nodo.matriz,
                (xI, yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posicion
            if not (hijo.validarPerder()):  # Esto es cuando esta dentro de los enemigos
                cola.append(hijo)

        # derecha
        xI = x + 1
        yI = y

        if xI < matriz_juego.shape[1] and not ((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 3:
            nodos_visitados = nodo.nodos_visitados.copy()  # pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()
            print("Entre a derecha")
            hijo = Nodo(
                nodo.matriz,
                (xI, yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posicion
            if not (hijo.validarPerder()):  # Esto es cuando esta dentro de los enemigos
                cola.append(hijo)

    return "No hay solucion", nodos_creados, nodos_expandidos


print(amplitud(juego))
