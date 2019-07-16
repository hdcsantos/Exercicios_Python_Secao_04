print('Digito por linha')

numero = input('Digite um numero entre 1000 e 9999: ')

n = []

n.extend(numero)

for i in n:
    print(f"{i}")
