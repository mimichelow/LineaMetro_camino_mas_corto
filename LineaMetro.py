import csv

from typing import List


class LineaMetro:

    def __init__(self, filename: str = "network.csv"):
        self.LineaMetro = {}
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                parada = row["PARADA"]
                color = row["COLOR"]
                lineas = row["LINEAS"].split(",")
                vecinos = row["VECINOS"].split(",")
                self.LineaMetro[parada] = {
                    "COLOR": color,
                    "LINEAS": lineas,
                    "VECINOS": vecinos
                }

    @staticmethod
    def respuestaMasCorta(respuestas: List[str]) -> str:
        temp = [x for x in respuestas if x]
        temp.sort(key=len)
        for path in temp:
            return path
        return ""

    def caminoMasCorto(self, inicio: str, final: str, color: str = "BLANCO") -> str:
        answer = []
        if inicio == "" or final == "":
            return answer

        # Algoritmo que busca el camino más corto de manera recursiva, auxiliar para caminoMasCorto
        def DFS(inicio: str, final: str, visitados: List, linea: int) -> str:
            # Definimos Casos Base
            if inicio in visitados[0]:
                return ""
            if self.LineaMetro[inicio]["COLOR"] == color or self.LineaMetro[inicio][
                "COLOR"] == "BLANCO" or color == "BLANCO":
                visitados[0] += inicio
            else:
                visitados[1] += inicio

            if final == inicio:

                return visitados[0]






            # Si la parada es visitable la agrega a visitados[0] de lo contrario a visitados[1], luego va a los
            # vecinos

            respuesta = []

            # Si la estación fue parada, vamos a todos los vecinos, de lo contrario vamos solo a los de la misma linea
            if inicio in visitados[0]:
                for vecino in self.LineaMetro[inicio]["VECINOS"]:
                    compartidos=[path for path in self.LineaMetro[inicio]["LINEAS"] if path in self.LineaMetro[vecino]["LINEAS"]]
                    for camino in compartidos:
                        temp = DFS(vecino, final, visitados.copy(), camino)
                        respuesta.append(temp)
            else:
                for vecino in self.LineaMetro[inicio]["VECINOS"]:
                    if linea in self.LineaMetro[vecino]["LINEAS"]:
                        temp = DFS(vecino, final, visitados.copy(), linea)
                        respuesta.append(temp)
            return LineaMetro.respuestaMasCorta(respuesta)

        # Necesitamos partir nuestro viaje en cada una de las lineas del metro a la cual pertenece la parada inicio
        for x in self.LineaMetro[inicio]["LINEAS"]:
            temp = DFS(inicio=inicio, final=final, visitados=["", ""], linea=x)
            # Nuestra respuesta es la más cortas de las respuestas no vacias, si todas son vacias, retorna vacio
            if temp:
                if not answer:
                    answer = temp
                else:
                    if len(answer) > len(temp):
                        answer = temp

        return answer
