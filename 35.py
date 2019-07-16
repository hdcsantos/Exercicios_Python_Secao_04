import math

print('Calcular a hipotenusa')
print("Informe os valores dos catetos de a e b")

a = int(input())
b = int(input())

soma = (a ** 2) + (b ** 2)
hipotenusa = soma ** 0.5

# hipotenusa = math.hypot(a, b)

# hipotenusa = math.sqrt(a * a + b * b)


print(f"A hipotenusa do triangulo em questão é {hipotenusa}")
          
