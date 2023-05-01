import numpy as np
from Nodo import Nodo

juego =np.array ([
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

def amplitud (matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    for i in range (matriz_juego.shape[0]): #filas
        for j in range(matriz_juego.shape[1]): #columnas
            if matriz_juego[i][j]== 2: #posicion del agente
                pos_agente = (j,i) #x=j(columnas), y=i(filas)
                matriz_juego[i][j] = 0 #actualizar
                break #romper ciclo para eficiencia
    raiz = Nodo(
        matriz_juego,
        pos_agente,
        [False], #condición de meta es igual al false porque no ha encontrado esferas
        [pos_agente], #Recorrido
        [pos_agente] #visitados
    )

    cola = [raiz]

    while len(cola) > 0: #condicion de parada
        nodo = cola.pop(0) #extraer el primero de la cola
        nodos_expandidos+=1
        
        if(nodo.condicionGanar()):
            return nodo.recorrido,nodos_creados,nodos_expandidos #Retorno la solución
        
        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        #genero los hijos
        

        #Arriba
        xI= x
        yI = y - 1

        if yI>=0 and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] !=1: 
            nodos_visitados = nodo.nodos_visitados.copy() #pasar por valor
            nodos_visitados.append(xI,yI)
            recorrido = nodo.recorrido.copy() #Evitar pasa por referencia
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz, #Compartido
                (xI,yI), #Nueva posicion
                estado,
                recorrido, #Nuevo
                nodos_visitados #Nuevo
            )
            nodos_creados+= 1
            hijo.marcar() #Evaluar que sucede en la posicion
            cola.append(hijo)

        #Abajo    
        xI= x
        yI = y + 1

        if yI<matriz_juego.shape[0] and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] !=1: 
            nodos_visitados = nodo.nodos_visitados.copy() #pasar por valor
            nodos_visitados.append(xI,yI)
            recorrido = nodo.recorrido.copy() #Evitar pasa por referencia
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,
                (xI,yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados+= 1
            hijo.marcar() #Evaluar que sucede en la posicion
            cola.append(hijo)

        #izquierda
        xI= x - 1
        yI = y 

        if xI>=0 and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] !=1: 
            nodos_visitados = nodo.nodos_visitados.copy() #pasar por valor
            nodos_visitados.append(xI,yI)
            recorrido = nodo.recorrido.copy() #Evitar pasa por referencia
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,
                (xI,yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados+= 1
            hijo.marcar() #Evaluar que sucede en la posicion
            cola.append(hijo)

        #derecha
        xI= x + 1
        yI = y 

        if xI<matriz_juego.shape[1] and not((xI,yI) in nodo.nodos_visitados) and nodo.matriz[y,x] !=1: 
            nodos_visitados = nodo.nodos_visitados.copy() #pasar por valor
            nodos_visitados.append(xI,yI)
            recorrido = nodo.recorrido.copy() #Evitar pasa por referencia
            recorrido.append((xI,yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,
                (xI,yI),
                estado,
                recorrido,
                nodos_visitados
            )
            nodos_creados+= 1
            hijo.marcar() #Evaluar que sucede en la posicion
            cola.append(hijo)

    return "No hay solucion",nodos_creados,nodos_expandidos

print(amplitud(juego))