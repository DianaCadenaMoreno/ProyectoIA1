# GOKU SMART

Este es el primer proyecto propuesto en el curso de inteligencia artificial que pretende implementar los distintos algoritmos de busqueda no informada(Amplitud,Costo Uniforme y Profundidad) e informada(Avara y a*) por medio del juego GOKU SMART, el agente inteligente (goku) tiene como objetivo encontrar las esferas para ganar, el ambiente se desarrolla en una matriz de 10x10 y la ruta que tome para llegar a la meta dependerá del algoritmo utilizado y estos se veran influenciados por los enemigos que se encuentren en la matriz y las semillas.

### Interfaz
Para poder ver los distintos tipos de algoritmos podra seleccionarlo en un menu desplegable y para ver los resultados obtenidos y movimientos deberá dar click en el boton de iniciar algoritmo. 

<p align="center">
    <img src="https://user-images.githubusercontent.com/95255931/237900790-8ba71de9-c69b-4ff2-9af3-fd056ea69ce9.jpeg">
</p>

### Git clone
```
git clone https://github.com/DianaCadenaMoreno/ProyectoIA1.git
```

### Dependencias

La aplicacion requiere: ```python 3.10.11``` ```numpy``` y ```PIL``` . Pueden instalarse mediante el archivo de requerimientos.

- Instalación del archivo ```requirements.txt```
```bash
pip install -r requirements.txt
```

### Ejecución 
Para ejecutar el archivo ```main.py```, se debe ubicar en la carpeta del programa y ejecutar el siguiente comando:
```bash
python main.py run
```

### Pruebas
Para realizar las pruebas en el proyecto hay una carpeta ```resources/maps``` en esa ruta se encuentran los archivos .txt este archivo se lee desde ```views/interfaz```y desde ```views/mapa```y se llama al iniciar los distintos algortimos: 

<p align="center">
    <img src="https://user-images.githubusercontent.com/95255931/238027015-b66b958f-06a4-4f4d-91cf-f21381865b8e.jpg">
</p>


### Creditos:
- Mayra sanchez - 2040506
- Laura Jaimes - 2040430
- Diana Cadena- 2041260
