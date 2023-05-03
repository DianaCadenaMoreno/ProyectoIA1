import numpy as np
from NodoProfundidad import Nodo

juego = np.array([
    [0, 0, 0, 0, 0, 0, 5],
    [0, 1, 2, 0, 2, 0, 2],
    [0, 0, 2, 3, 2, 0, 2],
    [0, 0, 2, 0, 2, 0, 2],
    [0, 3, 2, 0, 2, 0, 2],
    [0, 0, 2, 0, 2, 0, 2],
    [0, 0, 2, 0, 4, 0, 2] 
])

def busqueda_profundidad(juego):
    for i in range(0,juego.shape[0]):
        for j in range(0,juego.shape[1]):
            if juego[i,j] == 1:
                posAgente = (i,j)
                juego[i,j] = 0 #colocar la posicion como un espacio
                break #Salga del for

    root = Nodo(
        juego,
        posAgente,
        (False,False),
        [posAgente], #recorrido
        [posAgente] #visitados
    )
    pila = [root]
    nodos_expandidos= 1
    nodos_creados =1
    while True:
        nodo = pila.pop(-1) #quito el primer elemento
        nodos_expandidos +=1
        
        if (nodo.verificar_ganar()):
            return nodo.recorrido,nodos_expandidos,nodos_creados
        
        hijos = nodo.generar_hijos()
        for h in hijos:
            if not (h.verificar_perdi()):
                pila.append(h)
            nodos_creados +=1

        #condicion de no encontrar
        if len(pila)==0:
            return None,nodos_expandidos,nodos_creados
        
print(busqueda_profundidad(juego))
