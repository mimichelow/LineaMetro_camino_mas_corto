import csv
from LineaMetro import LineaMetro
from colorama import Fore

solucion = LineaMetro()
TestCases = []

# Carga los casos en TestCases.csv en formato input="Estacion de inicio,estacion final,color" output= "Resultado
# Esperado" y formatea en un arreglo con un diccionario con el estacion inicial, estacion final,color y resultado
# esperado del caso


with open("TestCases.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        TestCases.append({"inicio": row["Input"].split(",")[0],
                          "final": row["Input"].split(",")[1],
                          "color": row["Input"].split(",")[2],
                          "output": row["Output"].split(",")})
        if TestCases[-1]["output"] == [""]:
            TestCases[-1]["output"] = []

# Se prueban todos los TestCases en TestCases.csv
print(solucion.caminoMasCorto("L","H","BLANCO")+"asdf")
for x in TestCases:
    respuesta_de_caso = solucion.caminoMasCorto(x["inicio"], x["final"], x["color"])
    if not respuesta_de_caso:
        if x["output"] == respuesta_de_caso:
            print(Fore.GREEN+f"Caso {x} aceptado, no hay un camino válido")
        else:
            print(Fore.RED+f"Caso {x} rechazado, no se encontró un camino valido pero existía {x['output']}")
    elif respuesta_de_caso in x["output"]:
        print(Fore.GREEN+f"Caso {x} aceptado, la respuesta es {respuesta_de_caso}")
    else:
        print(Fore.RED+f"Caso {x} rechazado, la respuesta dada fue {respuesta_de_caso} pero se esperaba {x['output']}")
