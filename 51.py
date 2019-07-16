# Essa questão é referente ao cálculo da distância euclidiana entre dois pontos.
import math

print("x e y R²")
print("Origem (0,0)")

x1 = 0.0
y1 = 0.0

x2 = float(input('Informe a coordenada x2: '))
y2 = float(input('Informe a coordenada y2: '))

d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
# r = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

print(f'A distancia da coordenada x,y da sua origem (0,0) é de {round(d, 2)} unidades de comprimento.')
