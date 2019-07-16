print('Convertendo temperatura de ˚F para ˚C')
print('Informe a temperatura em ˚F: ')

fahrenheit = float(input())

celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print(f'A temperatura em ˚F ({fahrenheit}), convertida para ˚C é de {celsius}')
