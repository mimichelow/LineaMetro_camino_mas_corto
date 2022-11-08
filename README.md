# <p align="center"> **Que es este proyecto**
Se busca implementar un algoritmo de busqueda para la ruta más corta entre dos puntos para red de trenes/metro. Se implementa también un sistema de prueba de TestCases automático. Para resolver el problema se crea la clase [LineaMetro.py](LineaMetro.py) y el script [main.py](main.py) ambos programados en Python. También se usan los archivos [network.csv](/network.csv) y [TestCases.csv](TestCases.csv) para poblar el objeto LineaMetro y nuestros TestCases respectivamente.
## <p align="center"> **Generación de red de Metro**
Para modelar la red de metro a analizar se usa una lista de adyacencia. De esta manera el objeto LineaMetro contiene un diccionario donde la llave de cada entrada corresponde al nombre de la estación (En este caso se asume nombre único y de una sola letra, sensible a mayúsculas) conteniendo las entradas "COLOR", "LINEAS" y "VECINOS".  
>1. "COLOR": Esta entrada puede contener las strings "BLANCO", "ROJO" o "VERDE" según el color de la estáción.  
>2. "LINEAS": Contiene una lista que contiene todas las lineas a las que pertenece la estación.  
>3. "VECINOS": Contiene una lista de todos los nombres de las estaciones adyacentes.   

Estos estan contenidos en [network.csv](network.csv) y se rellenan de la siguiente manera: Cada fila contiene strings de la forma "AAAA","BBBB","####","CCCC" donde AAAA es una string con el nombre de una de las estaciones, BBBB es una string que indica su color, #### es una string que indica las lineas a la que pertenece esta estación. separadas por coma y CCCC indica el nombre de todas las estaciones aledañas separadas por coma.  
Como Ejemplo:
>LineaMetro["A"]["Lineas"] retorna la lista que contiene todas las lineas a las que pertenece la estación A

En este caso, el archivo [network.csv](network.csv) corresponde a la representación del siguiente diagrama: 

![Linea Metro ejemplo:](BUDA%20METRO.jpg)
## <p align="center"> **Algoritmo**  
Para encontrar le camino más corto entre las estaciones "A" y "B" usando un tren de color "COLOR" se llama a la función **self.caminoMasCorto(A,B,COLOR)** donde self indica el nombre de la instancia del objeto LineaMetro.  
La función caminoMasCorto retorna el camino más corto entre los vecinos de A y B, manteniendo la siguiente lógica. Al comenzar se ejecuta el algoritmo DFS en A, usando la ruta (A,B,+) para cada linea de A "+". **DFS()** si el nodo de inicio es una parada, agregandolo a la string de **visitados[0]** de lo contrario a **visitados[1]**, luego se busca recursivamente el camino más corto entre todos los nodos vecinos siguiendo la siguiente lógica. 
>- Si A ya fue una parada donde se detuvo, se retorna una respuesta vacía.   
>-  Si A fue una estación donde se detiene, se pasan a visitar todos los vecinos en todas las rutas donde se comparte línea, de lo contrario solo se pasa a un vecino en la misma línea, siguiendo esta misma línea.   
>-  Al encontrar que el nodo de inicio es igual al de término, se retorna **visitados[0]** el cual contiene todas las paradas anteriores para este camino.   
> 
La función auxiliar **respuestaMasCorta()** recibe una lista con las respuestas de todas las sub-rutas, para retornar solo la más corta de las respuestas no nulas. En caso de que todas sean nulas, se entrega la ruta "".
## <p align="center"> **Test Cases**  
Para implementar el uso de Tests Automaticos se usa el archivo [TestCases.csv](TestCases.csv) el cual contiene las columnas "Input" y "Output".  
>"Input": Contiene un String de la forma "AAA,BBB,CCC" donde AAA corresponde a la estación inicial, BBB a la estación final y CCC al color de el tren.  

>"Output": Contiene un String que corresponde a todas las soluciones del Input, separadas por coma.  

El script main luego toma estos Test Cases y ejecuta **caminoMasCorto** para cada uno, mostrando los resultados en consola en color rojo si es rechazado o verde si fue aceptada.  
En este caso el archivo presente corresponde a una lista de casos para la línea de metro ocupada como ejemplo. Los casos elegidos proponen casos de borde cómo:
- Estación de inicio está dentro de la ruta, pero el tren no se detiene.
- Ruta de una estación a si misma
- Ruta entre dos estaciones disconexas debido al color del tren.
- Ruta larga
- Ruta corta
- Color de parada inicial es distinto al de llegada
- Ruta sin comienzo o sin final.

## <p align="center"> **Codigo Ejemplo**
>import LineaMetro
> 
> p=LineaMetro()  
> print(p.caminoMasCorto("L","H","BLANCO"))
> 
> _____
>Output:
> 
> LABCH
## <p align="center"> **Ideas Finales**
Al abordar este problema se asumen ciertos supuestos como: 
1. Los valores de network y TestCases están saneados y siguen el formato apropiado.  
2. Un tren que comienza en una estación donde no para retorna la ruta hacia la meta sin incluir la ruta de inicio, pudiendo este ser un resultado inesperado si uno espera que esta sea una ruta invalida.
3. La red de metro tiene un tamaño apropiado para retornar un resultado en un tiempo apropiado, tomando en cuenta que este algoritmo tiene una complejidad de tiempo O(n^2)

