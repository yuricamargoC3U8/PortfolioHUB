import math  # Importar para usar a biblioteca de matematica do python.

x1 = float(input("Enter the x1 coordinate: "))
x2 = float(input("Enter the x2 coordinate: "))
y1 = float(input("Enter the y1 coordinate: "))
y2 = float(input("Enter the y2 coordinate: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("A distância entre os dois pontos é: ", distancia)
