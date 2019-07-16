"""
print("Numero invertido")

numero = input('Informe um numero a ser invertido: ')

print(f'O número {numero} invertido é {numero[::-1]}')
"""

numero = int(input('digite o número a ser invertido: '))
numero_lista = list(range(3))
numero_lista[0] = numero//100
numero_lista[1] = numero//10 - 10*(numero//100)
numero_lista[2] = numero - 10*(numero//10 - 10*(numero//100)) - 100*(numero//100)
print(numero_lista)
resultado = numero_lista[2]*100 + numero_lista[1]*10 + numero_lista[0]
print(f'o número invertido é: {resultado}')
