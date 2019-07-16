print('Premio investido')

pt = float(input("Valor do prêmio: "))
a1 = int(input("Valor de aposta do primeiro: "))
a2 = int(input("Valor de aposta do segundo: "))
a3 = int(input("Valor de aposta do terceiro: "))

r3_1 = 100 * a1 / pt
r3_2 = 100 * a2 / pt
r3_3 = 100 * a3 / pt

p1 = (pt / 100) * r3_1
p2 = (pt / 100) * r3_2
p3 = (pt / 100) * r3_3

print(f'Valor que o primeiro vai receber é de R$ {p1} reais \nValor que o segundo vai receber é de R$ {p2} reais '
      f'\nValor que o terceiro vai receber é de R$ {p3} reais')